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
from django.conf.urls import url
from django.contrib import admin
from app01 import views


# url由上到下判斷，且默認不須為完全匹配，所以為了怕出錯，會在網址後加$
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^fbv$', views.fbv),  # url => 函數
    url(r'^cbv$', views.Cbv.as_view()),  # url => 類
]
