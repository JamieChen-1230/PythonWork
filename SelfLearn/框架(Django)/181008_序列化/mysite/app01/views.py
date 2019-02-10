from django.shortcuts import render, HttpResponse
from app01 import models
import json


def serialization(request):
    return render(request, 'serialization.html', locals())


# 方式一
# def get_data(request):
#     user_list = models.UserInfo.objects.all()
#     return render(request, 'get_data.html', locals())

# 方式二
from django.core import serializers

def get_data(request):
    ret = {'status': True, 'data': None}
    try:
        # queryset<obj, obj>
        # user_list = models.UserInfo.objects.all()
        # ret['data'] = serializers.serialize('json', user_list)  # 用來序列化queryset<obj, obj>

        # queryset<{},{}> or queryset<(),()>
        # user_list = models.UserInfo.objects.all().values('id', 'username')
        user_list = models.UserInfo.objects.all().values_list('id', 'username')
        ret['data'] = list(user_list)
    except Exception as e:
        print(e)
        ret['status'] = False
    return HttpResponse(json.dumps(ret))