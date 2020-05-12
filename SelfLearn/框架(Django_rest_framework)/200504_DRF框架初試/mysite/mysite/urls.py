from django.conf.urls import url
from app01 import views


urlpatterns = [
    url(r'api/v1/dog', view=views.DogView.as_view()),
]
