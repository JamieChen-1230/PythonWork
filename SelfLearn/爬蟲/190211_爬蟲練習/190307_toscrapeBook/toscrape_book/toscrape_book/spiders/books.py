# -*- coding: utf-8 -*-
import scrapy
from scrapy.selector import Selector, HtmlXPathSelector
from scrapy.http import Request
from scrapy.http.cookies import CookieJar
# from ..items import BookItem


class BooksSpider(scrapy.Spider):
    name = 'books'
    allowed_domains = ['books.toscrape.com']
    start_urls = ['http://books.toscrape.com/']

    def parse(self, response):
        book_url_list = response.xpath("//ol[@class='row']//div[@class='image_container']/a/@href").extract()
        for i in book_url_list:
            url = "http://books.toscrape.com/" + i
            # print(url)
            yield Request(url=url, callback=self.get_book_inform)

    def get_book_inform(self, response):
        pass

