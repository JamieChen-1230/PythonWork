# from twisted.internet import reactor
# from scrapy.crawler import CrawlerRunner
# from scrapy.utils.project import get_project_settings
# from apscheduler.scheduler import Scheduler
# from django.core.cache import cache
# import time
# # 例項化
# sched = Scheduler()
#
#
# # 每隔600秒自動執行
# @sched.interval_schedule(seconds=10)
# def runing():
#     '''
#     get_project_settings() 方法會取得爬蟲專案中的 settings.py 檔案設定
#     啟動爬蟲前要提供這些設定給 Scrapy Engine
#     '''
#     runner = CrawlerRunner(get_project_settings())
#     d = runner.crawl('nba')
#     d.addBoth(lambda _: reactor.stop())
#     reactor.run()
#
# def main():
#     sched.start()