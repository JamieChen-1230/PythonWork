from django.shortcuts import render, HttpResponse
from django.http import JsonResponse
from app01 import models
import json


def imgs(request):
    # img_list = models.Img.objects.all()
    return render(request, "imgs.html", locals())


def get_imgs(request):
    # 透過nid可以
    nid = request.GET.get("nid")
    condition = {}
    condition["id__gt"] = int(nid)

    img_list = models.Img.objects.filter(**condition)[:10].values("id", "src", "title", "summary")
    img_list = list(img_list)
    ret = {
        "status": True,
        "data": img_list
           }
    # 兩種寫法都可以
    # return HttpResponse(json.dumps(ret))
    return JsonResponse(ret)
