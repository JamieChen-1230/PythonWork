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
        # print(nid)
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
    elif request.method == "POST":
        nid = request.GET.get('nid')  # class_id
        obj_cls = models.Classes.objects.get(id=nid)  # class對象
        # 注意：因為前端select multiple只能實現前端多選，傳到後台的值只有第一個，
        # 所以需要再前端搭配js寫迴圈，獲取所有值後，再傳到一個隱藏的input傳回來。
        str_t_id = request.POST.get('selected_item')  # 傳回來為字符串(EX: "1, 2")
        list_t_id = str_t_id.split(',')  # 轉成列表
        # print(list_t_id, type(list_t_id))
        # 重置(set)的參數若為一列表切記勿加 *
        obj_cls.ct.set(list_t_id)
        return redirect('/classes.html')
