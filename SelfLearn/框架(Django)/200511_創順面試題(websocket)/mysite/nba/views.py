from django.shortcuts import render
from nba import models, nba_crawler
from rest_framework import viewsets
from nba import serializers
from twisted.internet import reactor
from scrapy.crawler import CrawlerRunner
from scrapy.utils.project import get_project_settings
from dwebsocket.decorators import accept_websocket, require_websocket
from django.http import HttpResponse

# 在scrapy應用外調用spider
runner = CrawlerRunner(get_project_settings())
d = runner.crawl('nba')
d.addBoth(lambda _: reactor.stop())
reactor.run()


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


@accept_websocket
def websocket_msg(request):
    if not request.is_websocket():  # 判断是不是websocket连接
        # 如果是普通的http方法
        return render(request, 'index.html')
    else:
        # 透過bs4實現定時爬蟲，且有更新時提醒前端
        nba_crawler.main(request)
        for message in request.websocket:
            request.websocket.send(message)  # 發送信息到前端

