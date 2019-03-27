# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
from ..items import ChoutiItem
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
"""


class ChoutiSpider(scrapy.Spider):
    # 每一個爬蟲都有一個名字且唯一的，後面運行的時候也是通過這個名字來運行的
    name = 'chouti'
    # 允許爬取的域名
    allowed_domains = ['chouti.com']
    # 起始URL網址
    start_urls = ['http://dig.chouti.com/']
    # 設定成員變量cookie，以便之後調用
    cookie = None

    """
        重寫def start_requests()方法，可指定最開始處理請求的函數，默認為parse。
        這是scrapy根據父類的start_request()方法自動調用的，若要指定另一個方法為初始處理請求的函數，就必須覆寫start_request()方法
        def start_request(self):
                for url in self.start_urls:
                    yield Request(url, callback=self.xxx)
    """
    def parse(self, response):
        """
        登入抽屜
        :param response:
        :return:
        """
        # 創建cookie對象
        cookie_obj = CookieJar()
        # 獲取cookie
        cookie_obj.extract_cookies(response, response.request)
        # 將cookie存入成員變量
        self.cookie = cookie_obj._cookies

        # 發起登入請求
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
        """
        確認登入
        :param response:
        :return:
        """
        # 登入成功後開始獲取點讚url
        yield Request(
            url="https://dig.chouti.com/",
            callback=self.like_up
        )

    def like_up(self, response):
        """
        獲取欲點讚的文章URL，並點讚
        :param response:
        :return:
        """
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

    def show(self, response):
        """
        返回點讚結果
        :param response:
        :return:
        """
        print(response.text)
        item_obj = ChoutiItem(text=response.text)
        yield item_obj
