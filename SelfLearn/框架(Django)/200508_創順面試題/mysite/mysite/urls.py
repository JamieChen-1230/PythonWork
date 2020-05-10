from django.conf.urls import url
from django.contrib import admin
from newscrawler import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^index/', views.index),
    url(r'^content/', views.show_content),
]
