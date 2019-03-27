# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class BookItem(scrapy.Item):
    name = scrapy.Field()
    price = scrapy.Field()
    review_rating = scrapy.Field()  # 評價等級
    review_num = scrapy.Field()
    upc = scrapy.Field()  # 產品編碼
    stock = scrapy.Field()  # 庫存量
