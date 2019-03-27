# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http import Request


class PchomeSpider(scrapy.Spider):
    name = 'pchome'
    start_urls = ["https://shopping.pchome.com.tw/"]
    HEADERS = {
        # pchome 有檢察是否包含referer
        "Referer": "https://shopping.pchome.com.tw/",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36",
        "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8",
    }

    def parse(self, response):
        url = "https://ecshweb.pchome.com.tw/search/v3.3/all/results?q=msi&page=1&sort=sale/dc"
        yield Request(url=url, callback=self.item_list, headers=self.HEADERS)

    def item_list(self, response):
        # PChome的商品資料是放在https://ecshweb.pchome.com.tw/search/v3.3/all/results
        # 先用eval()將字符串response.text轉為字典形式
        # eval(response.text)["prods"] 為一陣列，裡面每筆資料為一字典
        for item in eval(response.text)["prods"]:
            print("商品名稱: " + item["name"])
            print(item["describe"])
            print("------------------------------------------")


