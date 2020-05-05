from django.conf.urls import url
from django.contrib import admin
from app01 import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^books/', views.books),
    url(r'^add_book/', views.add_book),
    url(r'^update_book/', views.update_book),
    url(r'^delete_book/', views.delete_book),
    url(r'^search_book/', views.search_book),
]
