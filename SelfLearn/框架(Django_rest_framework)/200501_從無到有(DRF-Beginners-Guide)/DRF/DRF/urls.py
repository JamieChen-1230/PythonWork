from django.conf.urls import url, include
from django.contrib import admin
from rest_framework.routers import DefaultRouter
from musics import views

# DRF 提供 DefaultRouter 讓我們快速建立 Routers 路由。
router = DefaultRouter()
# 註冊網址=> router.register(路徑, ViewSets)
router.register(r'music', views.MusicViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 網址都移到router的urls，這樣APP多時才不會搞混
    url(r'^api/', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^index', views.index),
]
