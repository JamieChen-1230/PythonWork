from django.shortcuts import render
from nba import models, nba_crawler
from rest_framework import viewsets
from nba import serializers
import time

# 自動定時爬蟲
nba_crawler.main()


class NewsViewSet(viewsets.ModelViewSet):
    queryset = models.News.objects.all()
    serializer_class = serializers.NewsSerializer  # 序列化類


# 主頁(焦點新聞列表)
def index(request):
    return render(request, "index.html", locals())


# 詳細頁(新聞詳情頁面)
def detail_content(request):
    nid = request.GET.get("nid")
    print(nid)
    return render(request, "detail_content.html", locals())
