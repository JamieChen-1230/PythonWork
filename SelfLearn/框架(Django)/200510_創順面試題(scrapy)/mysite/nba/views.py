from django.shortcuts import render
from nba import models, nba_crawler
from rest_framework import viewsets
from nba import serializers
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings

# 在scrapy應用外調用spider
runner = CrawlerRunner(get_project_settings())
d = runner.crawl('nba')
d.addBoth(lambda _: reactor.stop())
reactor.run()

# 透過bs4實現定時爬蟲
nba_crawler.main()


class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer  # 序列化類


# 主頁(焦點新聞列表)
def index(request):
    # nba_crawler.crawler()
    return render(request, "index.html", locals())


# 詳細頁(新聞詳情頁面)
def detail_content(request):
    nid = request.GET.get("nid")
    print(nid)
    return render(request, "detail_content.html", locals())


