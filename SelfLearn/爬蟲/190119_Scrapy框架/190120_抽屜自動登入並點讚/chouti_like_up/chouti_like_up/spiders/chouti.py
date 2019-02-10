# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http import Request
from scrapy.http.cookies import CookieJar


class ChoutiSpider(scrapy.Spider):
    name = 'chouti'
    allowed_domains = ['chouti.com']
    start_urls = [
        'https://dig.chouti.com/',
    ]
    cookie = None

    def parse(self, response):
        """創建CookieJar對象"""
        cookie_obj = CookieJar()
        """獲取cookies"""
        cookie_obj.extract_cookies(response, response.request)
        # print(cookie_obj._cookies)
        self.cookie = cookie_obj._cookies  # 存到成員變量中

        """帶上用戶名密碼+cookie登入"""
        yield Request(
            url="https://dig.chouti.com/login",
            method="POST",
            headers={
                "content-type": "application/x-www-form-urlencoded; charset=UTF-8",
            },
            # 這裡的請求體不能用字典格式
            body="phone=886918207171&password=jamie851230&oneMonth=1",
            cookies=cookie_obj._cookies,
            callback=self.check_login,
        )

    def check_login(self, response):
        print(response.text)
        """登入成功後開始獲取點讚url"""
        yield Request(
            url="https://dig.chouti.com/",
            callback=self.like_up
        )

    def like_up(self, response):
        # 找到有share-linkid的div的share-linkid
        id_list = Selector(response=response).xpath("//div[@share-linkid]/@share-linkid").extract()
        # 當前頁的所有文章id
        for nid in id_list:
            url = "https://dig.chouti.com/link/vote?linksId=%s" % nid
            yield Request(
                url=url,
                method="POST",
                cookies=self.cookie,
                callback=self.show,
            )

        # page_urls = Selector(response=response).xpath("//div[@id='dig_lcpage']//a/@href").extract()
        # for page in page_urls:
        #     url = "https://dig.chouti.com%s" % page
        #     yield Request(
        #         url=url,
        #         callback=self.like_up,
        #     )

    def show(self, response):
        print(response.text)


