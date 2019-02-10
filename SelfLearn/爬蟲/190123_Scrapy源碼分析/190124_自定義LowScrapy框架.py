from twisted.internet import reactor    # 事件循環(可理解為select+while)，終止條件:所有socket皆移除
from twisted.web.client import getPage  # 創建Socket對象(如果下載完成會自動從事件循環中移除)
from twisted.internet import defer      # defer.Deferred => 特殊的Socket對象(不會發請求，故需手動移除)


class HttpResponse(object):
    """
    封裝回傳的response
    """
    def __init__(self, content, request):
        self.content = content
        self.request = request
        self.url = request.url
        self.text = str(content, encoding="utf-8")

class Request(object):
    """
    封裝request
    """
    def __init__(self, url, callback):
        self.url = url
        self.callback = callback

class ChoutiSpider(object):
    name = "chouti"

    def start_requests(self):
        start_urls = ["http://www.baidu.com", "http://www.bing.com"]
        for url in start_urls:
            yield Request(url, callback=self.parse)

    def parse(self, response):
        print(response.url)  # response是下載頁面
        yield Request(url="http://www.google.com", callback=self.parse)

import queue
"""暫時當作調度器的存放位置"""
Q = queue.Queue()

class Engine(object):

    def __init__(self):
        self._close = None
        self.max = 5
        self.crawling = []

    def get_response_callback(self, content, request):
        self.crawling.remove(request)
        """封裝response"""
        rep = HttpResponse(content, request)
        """執行外邊spider定義的callback函數"""
        result = request.callback(rep)  # request.callback()等於自定義的callback，在這是parse()
        import types
        """若還有yield則需再把他們加入調度器"""
        if isinstance(result, types.GeneratorType): # 若有回傳值且回傳的是生成器則執行
            for req in result:
                # 照理來講應該還要判斷是Item對象還是Request對象，在這我們當他只會返回Request對象
                if isinstance(req, Request):
                    Q.put(req)
                else:
                    pass

    def _next_request(self):
        """
        去取Request對象，並發送請求
        """
        """終止條件"""
        # print(self.crawling, Q.qsize())
        if Q.qsize() == 0 and len(self.crawling) == 0:  # 調度器和執行中的陣列皆為空時執行
            self._close.callback(None)  # 關閉_close(特殊socket對象)
            return

        """最大併發數限制"""
        if len(self.crawling) >= self.max:  # 如果超過最大併發數表示不需再向執行中的陣列添加任務
            return

        """從取調度器中取Request對象，並發送請求"""
        while len(self.crawling) < self.max:
            try:  # 若為非阻塞，取不到值則報錯
                req = Q.get(block=False)  # block=False:表不阻塞，從隊列取東西時默認是會等的
                """添加任務至執行中的陣列"""
                self.crawling.append(req)
                """利用getPage創建socket"""
                d = getPage(req.url.encode("utf-8"))
                """get_response_callback()作用: 調用用戶spider中定義的callback方法，並將新請求添加到調度器"""
                d.addCallback(self.get_response_callback, req)
                """為達到最大併發數，當結束一個任務後要再去調度器獲取新的Request"""
                d.addCallback(lambda _:reactor.callLater(0, self._next_request))
            except Exception as e:
                # print(e)
                return

    @defer.inlineCallbacks
    def crawl(self, spider):
        """將起始url之Request對象放入調度器(Q隊列)"""
        start_requests = iter(spider.start_requests())
        while True:
            try:
                request = next(start_requests)
                Q.put(request)
            except StopIteration as e:
                break
        """去調度器取Request，並發請求"""
        # self._next_request()
        reactor.callLater(0, self._next_request)  # scrapy內部的調用方式

        self._close = defer.Deferred()
        yield self._close

_active = set()
engine = Engine()  # 創建引擎對象
spider = ChoutiSpider()  # 創建爬蟲對象

d = engine.crawl(spider)  # 運行爬蟲
_active.add(d)

"""監聽socket，並請求完成時移除"""
dd = defer.DeferredList(_active)
dd.addBoth(lambda _:reactor.stop())  # addBoth() => 當事件完成(addCallback)或失敗(addErrback)時調用
# def done(*args, **kwargs):
#     reactor.stop()
# dd.addBoth(done)

"""開始事件循環(內部發送請求，並接收響應，當所有socket請求完成後，終止事件循環)"""
reactor.run()
