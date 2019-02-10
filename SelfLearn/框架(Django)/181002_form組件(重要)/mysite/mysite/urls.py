"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from app01 import views
from app02 import views as views2
from app03 import views as views3
from app04 import views as views4

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    # 基礎表單組件
    url(r'^basis_form.html/', views.basis_form),
    # 基礎form組件結合sql應用
    url(r'^app01/', include('app01.urls')),
    # form組件之詳解字段
    url(r'^detailed_form.html/', views2.detailed_form),
    # form組件之動態綁定數據
    url(r'^dynamic_form.html/', views2.dynamic_form),
    # form組件之Ajax
    url(r'^ajax.html/', views3.ajax),
    # form組件之擴展
    url(r'^expansion.html/', views4.expansion),
]
