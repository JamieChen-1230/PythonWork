from engine import Request


class CnblogsSpider(object):
    name = "cnblogs"

    def start_requests(self):
        start_urls = ["http://www.cnblogs.com"]
        for url in start_urls:
            yield Request(url, callback=self.parse)

    def parse(self, response):
        print(response.url)  # response是下載頁面
        yield Request(url="http://www.cnblogs.com", callback=self.parse)
