# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class MyscrapyPipeline(object):  # 要先在settings裡配置才可調用

    # ----------舉例----------
    # def __init__(self, conn_str):
    #     self.conn_str = conn_str
    #
    # @classmethod
    # def from_crawler(cls, crawler):
    #     """
    #     創建Pipeline對象
    #     """
    #     conn = crawler.settings.get('DB')  # 可這樣連接數據庫
    #     return cls(conn)

    def open_spider(self, spider):
        """
        爬蟲開始執行時調用
        """
        print("open")
        self.f = open("news.txt", "a", encoding="utf-8")

    def close_spider(self, spider):
        """
        爬蟲結束執行時調用
        """
        print('close')
        self.f.close()

    def process_item(self, item, spider):
        """
        每當數據要被持久化時會被調用
        """
        tpl = "%s\n%s\n\n" % (item["title"].strip(), item["href"])
        # print(tpl)
        self.f.write(tpl)
        return item  # 會交給下一個序位的pipeline繼續運行
        # raise DropItem()  # 丟棄，不會交給下一個序位的pipeline


class MyscrapyPipeline2(object):  # 要先在settings裡配置才可調用

    # ----------舉例----------
    # def __init__(self, conn_str):
    #     self.conn_str = conn_str
    #
    # @classmethod
    # def from_crawler(cls, crawler):
    #     """
    #     創建Pipeline對象
    #     """
    #     conn = crawler.settings.get('DB')  # 可這樣開啟數據庫
    #     return cls(conn)

    def open_spider(self, spider):
        """
        爬蟲開始執行時調用
        """
        print("open2")
        self.f = open("news2txt", "a", encoding="utf-8")

    def close_spider(self, spider):
        """
        爬蟲結束執行時調用
        """
        print('close2')
        self.f.close()

    def process_item(self, item, spider):
        """
        每當數據要被持久化時會被調用
        """
        tpl = "%s\n%s\n\n" % (item["title"].strip(), item["href"])
        # print(tpl)
        self.f.write(tpl)
        raise DropItem()
