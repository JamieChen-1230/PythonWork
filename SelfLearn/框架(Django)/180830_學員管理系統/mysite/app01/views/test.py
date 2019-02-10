from django.shortcuts import render, HttpResponse
from app01 import models

def practice(request):
    # ret = models.Students.objects.filter(cs__name='全棧1班')
    # print(ret)

    # obj = models.Classes.objects.filter(name='全棧1班')[0]
    # print(obj.students_set.all())

    # obj_cls = models.Classes.objects.filter(id=17)[0]
    # obj_cls.ct.add(*[1, 2, 3])

    # list_cls = models.Classes.objects.filter(ct__name='t1')
    # list_cls_name = list_cls.values('name')
    # print(list_cls_name)

    # obj_t = models.Teachers.objects.get(id=2)
    # obj_t.classes_set.add(*[1, 2, 17])

    # list_cls = models.Classes.objects.all().values('id', 'name', 'ct', 'ct__name')
    #     # print(list_cls)

    list_t = models.Teachers.objects.all().values('id', 'name', 'classes_set__name')

    return HttpResponse('test')
