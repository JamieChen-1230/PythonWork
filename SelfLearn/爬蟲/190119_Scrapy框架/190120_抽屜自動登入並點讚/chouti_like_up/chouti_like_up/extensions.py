from scrapy import signals


class MyExtend:
    def __init__(self, crawler):
        self.crawler = crawler
        # 在指定信號上註冊操作
        self.crawler.signals.connect(self.start, signals.engine_started)  # signals.xxx 信號
        self.crawler.signals.connect(self.start, signals.spider_closed)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(crawler)

    # ---------操作---------
    def start(self):
        print("signals.engine_started.start....")

    def close(self):
        print("spider close.....")
