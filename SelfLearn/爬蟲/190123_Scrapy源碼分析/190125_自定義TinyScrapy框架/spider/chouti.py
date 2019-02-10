from engine import Request


class ChoutiSpider(object):
    name = "chouti"

    def start_requests(self):
        start_urls = ["http://www.baidu.com", "http://www.bing.com"]
        for url in start_urls:
            yield Request(url, callback=self.parse)

    def parse(self, response):
        print(response.url)  # response是下載頁面
        yield Request(url="http://www.google.com", callback=self.parse)
