from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from nba import views


# DRF 提供 DefaultRouter 讓我們快速建立 Routers 路由。
router = DefaultRouter()
# 註冊網址 => router.register(路徑, ViewSets)
router.register(r'news', views.NewsViewSet)


urlpatterns = [
    url(r'^$', views.index),
    url(r'^content', views.detail_content),
    url(r'^websocket_msg$', views.websocket_msg),
    url(r'^admin/', admin.site.urls),
    url(r'^api/', include(router.urls)),
]
