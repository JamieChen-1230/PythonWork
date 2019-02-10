from django.conf.urls import url, include
from django.contrib import admin
from app01 import views


urlpatterns = [
    # 基礎form組件結合sql應用
    url(r'^users.html/', views.users),
    url(r'^add_user.html/', views.add_user),
    url(r'^edit_user.html_(\d+)/', views.edit_user),
]