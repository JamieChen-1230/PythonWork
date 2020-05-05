# 總路由分發
from django.conf.urls import url, include
from django.contrib import admin
from app01 import views

# url(正則表達式, views視圖函數, 參數, 別名)
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # -----最基本的url配置(正則表達式, views視圖函數)-----
    url(r'^show_time$', views.show_time),  # ^ 匹配字符串須為網址開頭, $ 須為網址結尾
    url(r'^login/', views.login),
    # -----進階路由分發(include(欲分配至的url檔))-----
    url(r'^app01/', include('app01.urls')),  # 有關app01的網址都移到app01的urls，這樣APP多時才不會搞混
]
