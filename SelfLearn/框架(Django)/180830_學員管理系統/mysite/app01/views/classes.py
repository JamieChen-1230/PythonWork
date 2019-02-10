from django.shortcuts import render, redirect
from app01 import models

def get_classes(request):
    list_cls = models.Classes.objects.all()
    
    return render(request, 'get_classes.html', locals())


def add_classes(request):
    if request.method == 'GET':
        return render(request, 'add_classes.html')
    elif request.method == 'POST':
        title = request.POST.get('title')
        models.Classes.objects.create(name=title)
        return redirect('/classes.html')  # 裡面放url路徑


def del_classes(request):
    nid = request.GET.get('nid')
    models.Classes.objects.filter(id=nid).delete()
    return redirect('/classes.html')


def update_classes(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj_cls = models.Classes.objects.get(id=nid)
        return render(request, 'update_classes.html', locals())
    elif request.method == "POST":
        nid = request.POST.get('nid')
        name = request.POST.get('title')
        models.Classes.objects.filter(id=nid).update(name=name)
        return redirect('/classes.html')


def set_teachers(request):
    if request.method == 'GET':
        nid = request.GET.get('nid')
        obj_cls = models.Classes.objects.filter(id=nid)[0]
        list_cls_t = obj_cls.ct.all()
        list_t = models.Teachers.objects.all()
        return render(request, 'set_teachers.html', locals())
    elif request.method =="POST":
        nid = request.GET.get('nid')
        list_t_id = request.POST.get('ct')
        obj_cls = models.Classes.objects.get(id=nid)
        obj_cls.ct.set(*list_t_id)
        return redirect('/classes.html')
