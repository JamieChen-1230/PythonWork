from django.conf.urls import url
from django.contrib import admin
from api import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^api/v1/auth/$', view=views.AuthView.as_view()),
    url(r'^api/v1/order/$', view=views.OrderView.as_view()),
    url(r'^api/v1/userinfo/$', view=views.UserInfoView.as_view()),
]
