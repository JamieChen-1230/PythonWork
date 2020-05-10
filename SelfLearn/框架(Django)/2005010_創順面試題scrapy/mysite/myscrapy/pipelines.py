# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from nba import models


class NewsPipeline(object):
    def process_item(self, item, spider):
        # print(item)
        new_obj = models.News.objects.filter(**item).first()
        if new_obj:
            print("scrapy 資料已存在")
            return item
        print("scrapy 存入DB")
        models.News.objects.create(**item)
        return item
