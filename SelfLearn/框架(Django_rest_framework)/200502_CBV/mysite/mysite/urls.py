from django.conf.urls import url
from django.contrib import admin
from app01 import views

"""
CBV調用流程：url -> xxxView.as_view() -> 返回一個view方法 -> dispatch方法(反射) -> 執行動作(get, put等)
"""
urlpatterns = [
    # url(r'^admin/', admin.site.urls),
    url(r'^students/', views.StudentsView.as_view()),  # 固定寫法
]
