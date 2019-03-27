# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exceptions import DropItem


class DuplicatePipeline(object):  # 去重
    def __init__(self):
        self.myset = set()

    def process_item(self, item, spider):
        text = item["text"]
        if text in self.myset:
            raise DropItem("Duplicate text")

        self.myset.add(text)
        return item


class SavePipeline(object):  # 要先在settings裡配置才可調用
    """
    不必繼承特定的基類，只需實現特定之方法，如open_spider, close_spider, process_item等
    """

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
        爬蟲開始執行時調用，通常用來完成初始化工作，如：連接資料庫
        """
        print("PipelineOn")
        self.f = open("likeup.txt", "a", encoding="utf-8")

    def close_spider(self, spider):
        """
        爬蟲結束執行時調用，通常用來完成結束工作，如：關閉資料庫
        """
        print('PipelineClose')
        self.f.close()

    def process_item(self, item, spider):
        """
        每當數據要被持久化時會被調用(必須實現此方法)
        """
        tpl = "%s\n" % item["text"]
        self.f.write(tpl)
        # 如果返回了一個item表示會交給下一個序位的item pipeline(如果有的話)繼續運行
        return item
        # 如果拋出了DropItem()異常，表示丟棄此item，不會交給下一個序位的item pipeline，通常是檢測到無效數據時使用
        # raise DropItem()
