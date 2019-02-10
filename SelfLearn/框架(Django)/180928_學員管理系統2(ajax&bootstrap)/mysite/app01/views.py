from django.shortcuts import render, HttpResponse
from app01 import models
import json


def students(request):
    stu_list = models.Students.objects.all()
    cls_list = models.Classes.objects.all()
    return render(request, 'students.html', locals())


def del_student(request):
    response = {'status': True, 'message': None, 'id': None}
    try:
        nid = request.GET.get('nid')
        models.Students.objects.filter(id=nid).delete()
    except Exception as e:
        response['status'] = False

    ret = json.dumps(response)
    return HttpResponse(ret)


def add_student(request):
    # print(request.POST)
    response = {'status': True, 'message': None, 'id': None}
    try:
        name = request.POST.get('user')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cs_id = request.POST.get('cls_id')
        obj = models.Students.objects.create(name=name, age=age, gender=gender, cs_id=cs_id)
        response['id'] = obj.id
    except Exception as e:
        response['status'] = False
        response['message'] = '用戶輸入錯誤'

    ret = json.dumps(response, ensure_ascii=False)
    return HttpResponse(ret)


def edit_student(request):
    response = {'status': True, 'message': None}
    try:
        nid = request.POST.get('nid')
        name = request.POST.get('user')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        cs_id = request.POST.get('cls_id')
        obj = models.Students.objects.filter(id=nid).update(name=name, age=age, gender=gender, cs_id=cs_id)
    except Exception as e:
        response['status'] = False
        response['message'] = '用戶輸入錯誤'

    ret = json.dumps(response, ensure_ascii=False)
    return HttpResponse(ret)


def classes(request):
    cls_list = models.Classes.objects.all()
    t_list = models.Teachers.objects.all()
    return render(request, 'classes.html', locals())


def add_class(request):
    response = {'status': True, 'message': None}
    # print(request.POST)
    cls = request.POST.get('cls_name')
    models.Classes.objects.create(name=cls)
    return HttpResponse(json.dumps(response))


def del_class(request):
    response = {'status': True, 'message': None}
    nid = request.POST.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return HttpResponse(json.dumps(response))


def edit_class(request):
    response = {'status': True, 'message': None}
    nid = request.POST.get('nid')
    cls = request.POST.get('cls_name')
    models.Classes.objects.filter(id=nid).update(name=cls)
    return HttpResponse(json.dumps(response))


def allot_teacher(request):
    response = {'status': True, 'message': None}
    nid = request.POST.get('nid')
    t_ids = request.POST.getlist('t_id')
    # print(t_ids)
    obj = models.Classes.objects.filter(id=nid)[0]
    obj.ct.set(t_ids)
    return HttpResponse(json.dumps(response))