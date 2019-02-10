from django.shortcuts import render, redirect, HttpResponse
from app01 import models


def get_students(request):
    list_stu = models.Students.objects.all()
    list_cls = models.Classes.objects.all()
    return render(request, 'get_students.html', locals())


def add_students(request):
    if request.method == "GET":
        list_cls = models.Classes.objects.all()
        return render(request, 'add_students.html', locals())
    elif request.method == "POST":
        name = request.POST.get('user')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        class_id = request.POST.get('cs')
        models.Students.objects.create(name=name, age=age, gender=gender, cs_id=class_id)
        return redirect('/students.html')


def ajax_add_students(request):
    name = request.POST.get('user')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    class_id = request.POST.get('cs')
    models.Students.objects.create(name=name, age=age, gender=gender, cs_id=class_id)
    return HttpResponse('ok')


def del_students(request):
    nid = request.GET.get('nid')
    models.Students.objects.filter(id=nid).delete()
    return redirect('/students.html')


def ajax_del_students(request):
    nid = request.GET.get("nid")
    models.Students.objects.filter(id=nid).delete()
    return HttpResponse('ok')


def update_students(request):
    if request.method == "GET":
        nid = request.GET.get('nid')
        obj_stu = models.Students.objects.get(id=nid)
        list_cls = models.Classes.objects.all()
        return render(request, 'update_students.html', locals())
    elif request.method == "POST":
        id = request.POST.get('nid')
        name = request.POST.get('user')
        age = request.POST.get('age')
        gender = request.POST.get('gender')
        class_id = request.POST.get('cs')
        models.Students.objects.filter(id=id).update(name=name, age=age, gender=gender, cs_id=class_id)
        return redirect('/students.html')


def ajax_update_students(request):
    id = request.POST.get('nid')
    name = request.POST.get('user')
    age = request.POST.get('age')
    gender = request.POST.get('gender')
    class_id = request.POST.get('cs')
    models.Students.objects.filter(id=id).update(name=name, age=age, gender=gender, cs_id=class_id)
    return HttpResponse('ok')