# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector
from scrapy.http import Request
from myscrapy.items import NewsItem


class NbaSpider(scrapy.Spider):
    name = 'nba'
    allowed_domains = ['nba.udn.com']
    start_urls = ['https://nba.udn.com/nba/index?gr=www']

    def parse(self, response):
        # print(response)
        news_body = Selector(response=response).xpath("//div[@id='news_body']")
        # print(news_body.extract())
        dt_list = news_body.xpath(".//dt")
        # print(dt_list.extract())
        news_list = []
        for dt in dt_list:
            # print(dt.xpath("@class").extract_first())
            if not dt.xpath("@class").extract_first() == "ads":
                # print(1)
                news_list.append(dt)
        # print(news_list)

        for new in news_list:
            # 紀錄item
            item = NewsItem()

            # 網址
            url = "https://nba.udn.com/" + new.xpath(".//a/@href").extract_first()
            item["url"] = url
            # print("url", url)
            # 圖片網址
            img_url = new.xpath(".//img/@src").extract_first()
            item["img_url"] = img_url
            # print("img_url", img_url)
            # 標題
            title = new.xpath(".//h3/text()").extract_first()
            item["title"] = title
            # print("title", title)
            # 大綱
            outline = new.xpath(".//p/text()").extract_first()
            item["outline"] = outline
            # print("outline", outline)

            yield Request(
                url=url,
                callback=self.detail,
                meta={'item': item},
            )

    def detail(self, response):
        # print(response.meta["item"])
        # 內容
        content_list = Selector(response=response).xpath("//div[@id='story_body_content']//p")
        content = ""
        for c in content_list:
            c_text = c.xpath("text()").extract_first()
            # print(c_text)
            if c_text and ("Imagesfacebook" not in c_text):
                content += c_text
        # print(content)
        item = response.meta["item"]
        item["content"] = content
        # print(item)

        # 上傳時間
        info_div = Selector(response=response).xpath("//div[@class='shareBar__info']")
        post_date = info_div.xpath(".//span/text()").extract_first()
        item["post_date"] = post_date
        # print(post_date)

        # 影片網址
        video_url = Selector(response=response).xpath("//div[@class='video-container']//iframe/@src").extract_first()
        item["video_url"] = video_url
        # print(item)
        # print(1)
        yield item

