from django.shortcuts import render, HttpResponse
from app01.models import *
from django.db.models import Q, F
from django.db.models import Avg,Min,Sum,Max,Count


def index(request):
    return render(request, 'index.html')


def searchbook(request):
    # ----------------聚合查詢----------------
    # 所有書的平均價格
    # avg_ret = Book.objects.all().aggregate(Avg('price'))
    # print(avg_ret)

    # 所有書的總價格
    # sum_ret = Book.objects.all().aggregate(Sum('price'))
    # print(sum_ret)

    # nb的書總價格，nb_money為自定義名稱
    # sum_ret = Book.objects.filter(authors__name='nb').aggregate(nb_money=Sum('price'))
    # print(sum_ret)

    # ----------------分組查詢----------------
    # 先用values分組，再用annotate個別進行處理
    # 個別作者出的書的總價
    # ret = Book.objects.values('authors__name').annotate(Sum('price'))
    # print(ret)
    # 每個出版社最便宜的書價格
    # ret = Book.objects.values('publish__name').annotate(Min('price'))
    # print(ret)

    # ----------------F&Q查詢----------------(可以跟一般查詢混用但要放在一般查詢前)
    # 幫現有的值加上固定值
    # Book.objects.all().update(price=F('price')+10)  # F('price')把現有的price抓出來
    # |或
    # ret = Book.objects.filter(Q(price=149) | Q(name='python')).values('name')
    # print(ret)
    # ~not
    # ret = Book.objects.filter(~Q(name='python')).values('name')
    # print(ret)
    return render(request, "index.html", locals())
