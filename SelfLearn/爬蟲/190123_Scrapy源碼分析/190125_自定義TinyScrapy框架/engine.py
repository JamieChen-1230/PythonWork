from twisted.internet import reactor    # 事件循環(可理解為select+while)，終止條件:所有socket皆移除
from twisted.web.client import getPage  # 創建Socket對象(如果下載完成會自動從事件循環中移除)
from twisted.internet import defer      # defer.Deferred => 特殊的Socket對象(不會發請求，故需手動移除)
from queue import Queue


class Request(object):
    """
    用於封裝用戶請求相關信息
    """
    def __init__(self, url, callback):
        self.url = url
        self.callback = callback


class HttpResponse(object):
    """
    用於封裝回傳用戶的response信息
    """
    def __init__(self, content, request):
        self.content = content
        self.request = request
        self.url = request.url
        self.text = str(content, encoding="utf-8")


class Scheduler(object):
    """
    任務調度器
    """
    def __init__(self):
        self.q = Queue()

    def next_request(self):
        """從調度器取出"""
        try:
            req = self.q.get(block=False)
        except Exception as e:
            req = None
        return req

    def enqueue_request(self, req):
        """放入調度器"""
        self.q.put(req)

    def size(self):
        return self.q.qsize()


class ExecutionEngine(object):
    """
    引擎: 包含所有的調度行為
    """
    def __init__(self):
        self._close = None
        self.scheduler = None
        self.max = 5
        self.crawlling = []

    @defer.inlineCallbacks
    def start(self):
        self._close = defer.Deferred()
        yield self._close

    def get_response_callback(self, content, request):
        self.crawlling.remove(request)
        response = HttpResponse(content, request)
        result = request.callback(response)
        import types
        if isinstance(result, types.GeneratorType):
            for req in result:
                self.scheduler.enqueue_request(req)

    def _next_request(self):
        if len(self.crawlling) == 0 and self.scheduler.size() == 0:
            self._close.callback(None)
            return

        """最大併發數限制"""
        if len(self.crawlling) >= self.max:  # 如果超過最大併發數表示不需再向執行中的陣列添加任務
            return

        while len(self.crawlling) < self.max:
            req = self.scheduler.next_request()
            if not req:
                return
            self.crawlling.append(req)
            d = getPage(req.url.encode("utf-8"))
            d.addCallback(self.get_response_callback, req)
            d.addCallback(lambda _: reactor.callLater(0, self._next_request))

    @defer.inlineCallbacks
    def open_spider(self, start_requests):
        self.scheduler = Scheduler()
        while True:
            try:
                req = next(start_requests)
            except StopIteration as e:
                break
            self.scheduler.enqueue_request(req)
        reactor.callLater(0, self._next_request)
        yield None  # 什麼都不返回，只是為了遵循@defer.inlineCallbacks的規則


class Crawler(object):
    """
    用於封裝調度器以及引擎等
    """
    def _create_engine(self):
        return ExecutionEngine()

    def _create_spider(self, spider_cls_path):
        module_path, cls_name = spider_cls_path.rsplit(".", maxsplit=1)
        import importlib
        m = importlib.import_module(module_path)
        cls = getattr(m, cls_name)
        return cls()

    @defer.inlineCallbacks
    def crawl(self, spider_cls_path):
        engine = self._create_engine()
        spider = self._create_spider(spider_cls_path)
        start_requests = iter(spider.start_requests())
        yield engine.open_spider(start_requests)
        yield engine.start()


class CrawlerProcess(object):
    """
    開啟事件循環
    """
    def __init__(self):
        self._active = set()

    def crawl(self, spider_cls_path):
        """
        創建crawler對象
        :param spider_cls_ptath:
        :return:
        """
        crawler = Crawler()
        d = crawler.crawl(spider_cls_path)
        self._active.add(d)

    def start(self):
        dd = defer.DeferredList(self._active)
        dd.addBoth(lambda _: reactor.stop())
        reactor.run()


class Command(object):

    def run(self):
        crawl_process = CrawlerProcess()
        spider_cls_path_list = [
            "spider.chouti.ChoutiSpider",
            "spider.cnblogs.CnblogsSpider",
        ]
        for spider_cls_path in spider_cls_path_list:
            crawl_process.crawl(spider_cls_path)
        crawl_process.start()


if __name__ == "__main__":
    cmd = Command()
    cmd.run()
