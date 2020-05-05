from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'show_time/', views.show_time, name='show_time'),
    url(r'^variable/', views.variable),
    url(r'^label/', views.label),
]
