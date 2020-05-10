# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsItem(scrapy.Item):
    title = scrapy.Field()
    outline = scrapy.Field()
    url = scrapy.Field()
    img_url = scrapy.Field()
    content = scrapy.Field()
    post_date = scrapy.Field()
    video_url = scrapy.Field()
