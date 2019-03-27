# -*- coding: utf-8 -*-
import scrapy
import sys
import io
from scrapy.selector import Selector
from scrapy.http import Request
from ..items import ChoutiItem
# from scrapy.dupefilter import RFPDupeFilter

# windows終端的問題，需設置這行才能順利顯示
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="gb2312")


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'  # 每一個爬蟲都有一個名字且唯一的，後面運行的時候也是通過這個名字來運行的
    allowed_domains = ['chouti.com']
    start_urls = [
        'http://dig.chouti.com/',
    ]

    # visited_urls = set()  # 自己定義用來去重的

    def parse(self, response):
        """
        這是scrapy根據父類的start_request()方法自動調用的，若要指定另一個方法為初始處理請求的函數，就必須覆寫start_request()方法
        def start_request(self):
                for url in self.start_urls:
                    yield Request(url, callback=self.xxx)
        """
        """
            // 表示子孫中
            .// 表當前對象的子孫中
            / 兒子
            /div 兒子中的div標籤
            /div[@class="li"] 兒子中的div標籤且id="li"
            /div[@id="li"] 兒子中的div標籤且class="li"
            /div[@id="li"][@class="li"] 雙條件:兒子中的div標籤且class="li"且class="li"
            //div/text() 獲取div標籤的文本
            //a/@href 獲取a標籤的href屬性
            //a[contains(@href, '/all/hot/recent/')]  找到href裡有包含/all/hot/recent/的所有a標籤
            //a[starts-with(@href, '/all/hot/recent/')]  找到href開頭為/all/hot/recent/的所有a標籤
            //a[re:test(@href, '/all/hot/recent/\d+')]  用正則找到href為/all/hot/recent/\d+的所有a標籤
            obj.extract() 列表中的每一個對象轉為字符串 => 返回整個列表
            obj.extract_first() 列表中的每一個對象轉為字符串 => 返回列表的第一個元素

            重寫def start_requests()方法，可指定最開始處理請求的函數，默認為parse
            """

        """找出所有標題名稱"""
        # # //表找後代；/表找子代
        # hxs = Selector(response=response).xpath("//div[@id='content-list']/div[@class='item']")
        # # print(hxs)
        # for obj in hxs:
        #     # .//表找當前標籤的後代
        #     a = obj.xpath(".//a[@class='show-content color-chag']/text()").extract()[0]
        #     print(a.strip())

        """找出當前頁面能顯示的所有頁碼"""
        # # hxs = Selector(response=response).xpath("//div[@id='page-area']//a/@href").extract()
        # # hxs = Selector(response=response).xpath(
        # #     "//a[starts-with(@href, '/all/hot/recent/')]/@href").extract()
        # hxs = Selector(response=response).xpath(
        #     "//a[re:test(@href, '/all/hot/recent/\d+')]/@href").extract()
        # for url in hxs:
        #     """將網址進行加後再存到數據庫，就能解決網址過長導致效率變慢的問題"""
        #     md5_url = self.md5(url)
        #     if md5_url in self.visited_urls:
        #         print("url已存在", url)
        #     else:
        #         self.visited_urls.append(md5_url)
        #         print(url)

        """找出網站的所有頁碼"""
        # # hxs = Selector(response=response).xpath("//div[@id='page-area']//a/@href").extract()
        # # hxs = Selector(response=response).xpath(
        # #     "//a[starts-with(@href, '/all/hot/recent/')]/@href").extract()
        # hxs = Selector(response=response).xpath(
        #     "//a[re:test(@href, '/all/hot/recent/\d+')]/@href").extract()
        # for url in hxs:
        #     """將網址進行加後再存到數據庫，就能解決網址過長導致效率變慢的問題"""
        #     md5_url = self.md5(url)
        #     if md5_url in self.visited_urls:
        #         print("url已存在", url)
        #     else:
        #         self.visited_urls.append(md5_url)
        #         url = "https://dig.chouti.com%s" % url
        #         print(url)
        #         """深度查找(引擎會將要訪問的新url加入調度器，callback為url要調用哪個函數)"""
        #         yield Request(url=url, callback=self.parse)

        """找出網站的所有頁碼"""
        print(response.url)
        hxs = Selector(response=response).xpath("//div[@id='content-list']/div[@class='item']")
        for obj in hxs:
            title = obj.xpath(".//a[@class='show-content color-chag']/text()").extract_first()
            href = obj.xpath(".//a[@class='show-content color-chag']/@href").extract_first()
            """items做格式化"""
            item_obj = ChoutiItem(title=title, href=href)
            """將item_obj加入pipeline，pipeline做持久化"""
            yield item_obj  # scrapy會根據yield的回傳類別判斷該傳到哪

        hxs2 = Selector(response=response).xpath("//div[@id='page-area']//a/@href").extract()
        for url in hxs2:
            # -----自己判斷去重-----
            # """將網址進行加後再存到數據庫，就能解決網址過長導致效率變慢的問題"""
            # md5_url = self.md5(url)
            # if md5_url in self.visited_urls:
            #     # print("url已存在", url)
            #     pass
            # else:
            #     self.visited_urls.add(md5_url)
            #     url = "https://dig.chouti.com%s" % url
            #     # print(url)
            #     """深度查找(引擎會將要訪問的新url加入調度器，callback為url要調用哪個函數)"""
            #     yield Request(url=url, callback=self.parse)  # scrapy會根據yield的回傳類別判斷該傳到哪

            # -----透過myscrapy.duplication.MyFilter判斷去重(較好)，其實內建的也會去重-----
            url = "https://dig.chouti.com%s" % url
            """深度查找(引擎會將要訪問的新url加入調度器，callback為url要調用哪個函數)"""
            yield Request(url=url, callback=self.parse)  # scrapy會根據yield的回傳類別判斷該傳到哪

    def md5(self, url):
        import hashlib
        obj = hashlib.md5()
        obj.update(bytes(url, encoding="utf-8"))
        return obj.hexdigest()
