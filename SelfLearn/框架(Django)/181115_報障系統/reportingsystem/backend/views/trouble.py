from django.shortcuts import render, redirect, HttpResponse
from repository import models
from ..forms.trouble import TroubleMaker, TroubleKiller, TroubleDetail, TroubleSolution
import datetime
from django.db.models import Q
from ..auth.auth import check_login
import json


@check_login
def trouble_list(request):
    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    # --------------------------------------------------

    current_user_id = request.session["user_info"]["nid"]
    result = models.Trouble.objects.filter(user_id=current_user_id).order_by("status").only(
        "id", "title", "create_time", "status", "processor")
    return render(request, "backend_trouble_list.html", locals())


@check_login
def add_trouble(request):
    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    # --------------------------------------------------

    current_user_id = request.session["user_info"]["nid"]
    if request.method == "GET":
        obj = TroubleMaker()
    else:
        obj = TroubleMaker(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)  # title, detail
            dic = {
                "user_id": current_user_id,
                "create_time": datetime.datetime.now(),
                "status": 1,
            }
            dic.update(obj.cleaned_data)
            models.Trouble.objects.create(**dic)
            return redirect("/backend/trouble-list.html")
    return render(request, "backend_add_trouble.html", locals())


def remove_trouble(request, nid):
    models.Trouble.objects.filter(id=nid).delete()
    return redirect("/backend/trouble-list.html")


@check_login
def edit_trouble(request, nid):
    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    # --------------------------------------------------

    if request.method == "GET":
        trouble_obj = models.Trouble.objects.filter(id=nid, status=1).only("id", "title", "detail").first()  # 只有未處理才可編輯
        if not trouble_obj:
            return HttpResponse("已正在處理，無法修改")

        # 用initial不驗證，data會驗證(默認)
        obj = TroubleMaker({"title": trouble_obj.title, "detail": trouble_obj.detail})
        return render(request, "backend_edit_trouble.html", locals())
    else:
        obj = TroubleMaker(data=request.POST)
        if obj.is_valid():
            # update返回的是受影響的行數
            v = models.Trouble.objects.filter(id=nid, status=1).update(**obj.cleaned_data)
            # print(v)
            if not v:  # 因為有可能在你編輯時被接單
                return HttpResponse("已經被處理")
            else:
                return redirect("/backend/trouble-list.html")
        else:
            return render(request, "backend_edit_trouble.html", locals())


@check_login
def trouble_detail(request, nid):
    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    # --------------------------------------------------

    trouble_obj = models.Trouble.objects.filter(id=nid).first()
    obj = TroubleDetail(initial={
        "title": trouble_obj.title,
        "user": trouble_obj.user.nickname,
        "detail": trouble_obj.detail,
    })
    return render(request, "backend_trouble_detail.html", locals())


@check_login
def trouble_solution(request, nid):
    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    # --------------------------------------------------

    if request.method == "GET":
        trouble_obj = models.Trouble.objects.filter(id=nid).first()
        obj = TroubleSolution(initial={
            "title": trouble_obj.title,
            "detail": trouble_obj.detail,
            "solution": trouble_obj.solution,
        })
        return render(request, "backend_trouble_solution.html", locals())
    else:
        obj = TroubleSolution(request.POST)
        if obj.is_valid():
            models.Trouble.objects.filter(id=nid, status=3).update(pj=obj.cleaned_data.get("pj"))
            return redirect("/backend/trouble-list.html")
        else:
            return render(request, "backend_trouble_solution.html", locals())


@check_login
def trouble_kill_list(request):
    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    # --------------------------------------------------

    current_user_id = request.session["user_info"]["nid"]
    # 找出自己已處理的單和未處理的單
    result = models.Trouble.objects.filter(Q(processor_id=current_user_id) | Q(status=1)).order_by("status")
    return render(request, "backend_trouble_kill_list.html", locals())


@check_login
def kill_trouble(request, nid):
    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    # --------------------------------------------------

    current_user_id = request.session["user_info"]["nid"]
    if request.method == "GET":
        # 未被自己接單
        if not models.Trouble.objects.filter(id=nid, processor_id=current_user_id).count():
            v = models.Trouble.objects.filter(id=nid, status=1).update(processor_id=current_user_id, status=2)
            # 被搶單
            if not v:
                return HttpResponse("已被他人接走")

        trouble_obj = models.Trouble.objects.filter(id=nid).first()
        obj = TroubleKiller(initial={"title": trouble_obj.title, "detail": trouble_obj.detail, "solution": trouble_obj.solution})
        return render(request, "backend_kill_trouble.html", locals())
    else:
        # 檢查是否是處理者本人提交
        if not models.Trouble.objects.filter(id=nid, processor_id=current_user_id).count():
            return HttpResponse("請勿盜用別人名義發送消息")

        obj = TroubleKiller(request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            dic = {
                "status": 3,
                "solution": obj.cleaned_data["solution"],
                "solution_time": datetime.datetime.now(),
            }
            models.Trouble.objects.filter(id=nid, processor_id=current_user_id).update(**dic)
            return redirect("/backend/trouble-kill-list.html")
        else:
            print(obj.errors)
            return render(request, "backend_kill_trouble.html", locals())


@check_login
def trouble_report(request):
    # -----------------要有blog才可使用-----------------
    blog_id = request.session['user_info']['blog__nid']
    # --------------------------------------------------

    return render(request, "backend_trouble_report.html", locals())


def trouble_json_report(request):
    # ------------------獲取數據------------------
    # processor列表
    processor_list = models.Trouble.objects.filter(status=3).distinct().values("processor_id", "processor__nickname")
    # print(processor_list)
    response = []
    for processor in processor_list:
        # 執行原生sql語句
        from django.db import connection, connections
        cursor = connection.cursor()
        # strftime('%%Y-%%m-01', create_time): 2018-12-01
        # strftime('%%s',strftime('%%Y-%%m-01', create_time)): 1543622400(秒)
        # strftime('%%s',strftime('%%Y-%%m-01', create_time))*1000: 1543622400000(毫秒) => 這才是Highcharts要求的格式
        cursor.execute("""select strftime('%%s',strftime('%%Y-%%m-01', create_time))*1000, count(id) from repository_trouble where processor_id=%s group by strftime('%%Y-%%m', create_time)""", [processor.get("processor_id")], )
        result = cursor.fetchall()
        # print(processor.get("processor__nickname"), result)
        temp = {
            "name": processor.get("processor__nickname"),
            "data": result
        }
        response.append(temp)
    return HttpResponse(json.dumps(response))
