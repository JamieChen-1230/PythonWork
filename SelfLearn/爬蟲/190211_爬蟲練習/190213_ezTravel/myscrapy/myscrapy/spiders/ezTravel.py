# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
import re


class EztravelSpider(scrapy.Spider):
    name = 'ezTravel'
    start_urls = ["https://vacation.eztravel.com.tw/"]

    def parse(self, response):
        """
        找出所有地區URL
        """
        area_items = Selector(response=response).xpath("//div[@id='section-vacation-keyword']//ul[@class='keyItem']/li/div[@class='keywordItem']")
        # print(area_items[0])
        for area_item in area_items:
            area_as = area_item.xpath(".//a[contains(@href, '/vacation.eztravel.com.tw/pkgfrn/results/TPE/')]")
            for area_a in area_as:
                area_url = "https:" + area_a.xpath("./@href").extract_first() + "&avbl=1"
                yield Request(url=area_url, callback=self.page_url)

    def page_url(self, response):
        """
        行程挖掘+分頁挖掘
        """
        page_items = Selector(response=response).xpath("//div[@class='page-tfoot']//li/a")
        # print(page_items)
        for page in page_items:
            # print(page.xpath("./@title").extract_first())
            if re.match("第\\d+頁", page.xpath("./@title").extract_first()) and page.xpath("./@href"):
                url = "https://vacation.eztravel.com.tw" + page.xpath("./@href").extract_first()
                print(url)
                request = Request(url=url, callback=self.itinerary_url)
                area_num = re.search("/(?P<area>\d+)", url).group("area")
                # print(area_num)
                """把地區代碼封裝到request中，之後要用來判斷國家"""
                request.meta["area_num"] = area_num
                """行程挖掘"""
                yield request
                """分頁挖掘"""
                yield Request(url=url, callback=self.page_url)

    def itinerary_url(self, response):
        """
        找出所有行程之URL
        """
        # print("==>", response.meta["area_num"])
        itinerary_urls = Selector(response=response).xpath("//ul[@class='results-list']//a[@class='list-item-link'][re:test(@href, '^/pkgfrn/introduction/\w+')]/@href")
        for url in itinerary_urls:
            url = "https://vacation.eztravel.com.tw" + url.extract()
            # print(url)
            request = Request(url=url, callback=self.itinerary_content)
            request.meta["area_num"] = response.meta["area_num"]
            yield request

    def itinerary_content(self, response):
        """
        找出需要資訊
        """
        # print(response.meta["area_num"])
        basicInformation = Selector(response=response).xpath("//div[@class='product-info css-td']")
        Days = basicInformation.xpath("./div").extract()[0]
        Days = re.findall("\d+/\d+/\d+", Days.replace(" ", ""))
        fromDay = Days[0]
        toDay = Days[1]
        Citys = basicInformation.xpath("./div/div[@class='tag-box']/div[@class='tag']/h2/text()").extract()
        print(response.meta["area_num"], fromDay, toDay, Citys, response.url)
