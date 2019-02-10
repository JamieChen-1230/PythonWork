from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django import conf
from kingadmin import app_setup
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.db.models import Q
from kingadmin import form_handle
import json
from kingadmin import permissions

# 全局執行, 且啟動時自動執行
app_setup.kingadmin_auto_discover()
from kingadmin.sites import site

print("sites", site.enabled_admins)


def app_index(request):
    return render(request, "kingadmin/app_index.html", {"site": site})


@permissions.check_permission
def model_list(request, app_name):
    app_tables = site.enabled_admins[app_name]
    return render(request, "kingadmin/model_list.html", {"site": site,
                                                         "app_tables": app_tables,
                                                         "app_name": app_name})


@permissions.check_permission
@login_required
def model_obj_list(request, app_name, model_name):
    """取出指定model的數據返回給前端"""
    admin_class = site.enabled_admins[app_name][model_name]
    if request.method == "POST":
        selected_action = request.POST.get("action", "")
        selected_ids = json.loads(request.POST.get("selected_ids", ""))
        # print(selected_action, selected_ids)
        selected_objs = admin_class.model.objects.filter(id__in=selected_ids)
        # print(selected_objs)
        admin_action_func = getattr(admin_class, selected_action)
        if admin_action_func(request, selected_objs):
            # 有些action不用跳轉頁面(沒有回傳值)
            return admin_action_func(request, selected_objs)

    querysets = admin_class.model.objects.all().order_by("-id")
    # 過濾
    querysets, filter_conditions = get_filter_result(request, querysets)
    admin_class.filter_conditions = filter_conditions

    # 搜尋
    querysets, search_key = get_searched_result(request, querysets, admin_class)
    admin_class.search_key = search_key

    # 排序
    querysets, orderby_conditions = get_orderby_result(request, querysets, admin_class)
    admin_class.orderby_conditions = orderby_conditions

    # --------Django內置分頁--------
    paginator = Paginator(querysets, admin_class.list_per_page)  # Paginator(obj列表, 每頁幾條)
    page = request.GET.get('_page')  # 取得頁數

    try:
        querysets = paginator.page(page)
    except PageNotAnInteger:
        querysets = paginator.page(1)
    except EmptyPage:
        querysets = paginator.page(paginator.num_pages)
    # --------Django內置分頁--------

    return render(request, "kingadmin/model_obj_list.html", locals())


@permissions.check_permission
@login_required
def model_obj_change(request, app_name, model_name, obj_id):
    """kingadmin 數據修改"""
    # form_obj = form_handle.CustomerForm()

    admin_class = site.enabled_admins[app_name][model_name]
    # 動態生成model_form
    form_add = False
    model_form = form_handle.create_dynamic_model_form(admin_class, form_add)
    # 資料對象
    obj = admin_class.model.objects.filter(id=obj_id)[0]
    if request.method == "GET":
        # 實例化表單對象
        form_obj = model_form(instance=obj)
    elif request.method == "POST":
        # print("request.POST", request.POST)
        form_obj = model_form(instance=obj, data=request.POST)
        if form_obj.is_valid():  # 判斷資料是否合法
            form_obj.save()  # 資料更新
        return redirect("/kingadmin/%s/%s/" % (app_name, model_name))

    return render(request, "kingadmin/model_obj_change.html", locals())


@permissions.check_permission
@login_required
def model_obj_add(request, app_name, model_name):
    """kingadmin 數據添加"""
    admin_class = site.enabled_admins[app_name][model_name]
    # 動態生成model_form
    form_add = True
    model_form = form_handle.create_dynamic_model_form(admin_class, form_add)
    if request.method == "GET":
        # 實例化表單對象
        form_obj = model_form()
    elif request.method == "POST":
        print("request.POST", request.POST)
        form_obj = model_form(data=request.POST)
        if form_obj.is_valid():
            print("valid")
            form_obj.save()
        return redirect("/kingadmin/%s/%s/" % (app_name, model_name))

    return render(request, "kingadmin/model_obj_add.html", locals())


@permissions.check_permission
@login_required
def model_obj_delete(request, app_name, model_name, obj_id, objs_id):
    """kingadmin 數據刪除"""
    # print("idorids", obj_id, objs_id)
    admin_class = site.enabled_admins[app_name][model_name]
    obj = ""
    objs = ""
    if obj_id:
        obj = admin_class.model.objects.filter(id=obj_id)[0]
    elif objs_id:
        # 轉為id陣列
        objs_id = [i for i in objs_id.split(",")]
        objs_id.pop(-1)  # 去掉多餘的最後一項
        # print(objs_id)
        objs = admin_class.model.objects.filter(id__in=objs_id)

    if request.method == "POST":
        if obj_id:
            obj.delete()
        if objs_id:
            objs.delete()

        return redirect("/kingadmin/%s/%s/" % (app_name, model_name))
    return render(request, "kingadmin/model_obj_delete.html", locals())


def get_searched_result(request, querysets, admin_class):
    """搜尋過濾"""
    search_key = request.GET.get("_q", "")
    if search_key:
        q = Q()
        q.connector = "OR"
        for search_field in admin_class.search_fields:
            q.children.append(("%s__contains" % search_field, search_key))
        return querysets.filter(q), search_key
    return querysets, search_key


def get_orderby_result(request, querysets, admin_class):
    """排序過濾"""
    orderby_conditions = {}
    orderby_index = request.GET.get("_o", "")
    print(orderby_index)
    if orderby_index:
        orderby_key = admin_class.list_display[abs(int(orderby_index))]
        orderby_conditions[orderby_key] = orderby_index
        if orderby_index.startswith("-"):
            return querysets.order_by("-"+orderby_key), orderby_conditions
        return querysets.order_by(orderby_key), orderby_conditions
    return querysets, orderby_conditions


def get_filter_result(request, querysets):
    """條件過濾"""
    filter_conditions = {}
    for key, val in request.GET.items():
        if key in ("_page", "_o", "_q"):
            continue
        if val:
            filter_conditions[key] = val
    print("filter_conditions", filter_conditions)
    return querysets.filter(**filter_conditions), filter_conditions


def acc_login(request):
    if request.method == "GET":
        return render(request, "kingadmin/login.html")
    elif request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        error_msg = ""
        # ---------django自帶驗證登入---------
        # 驗證, 成功返回用戶對象
        user = authenticate(username=username, password=password)
        if user:
            print("passed authenticate", user)
            # 登入, 並將user寫入request.user
            login(request, user)
            next_url = request.GET.get("next", "/kingadmin/")  # .get("要取的key", "找不到時的默認值")
            return redirect(next_url)
        else:
            error_msg = "Wrong username or password"
            return render(request, "kingadmin/login.html", {"error_msg": error_msg})
        # ---------django自帶驗證登入---------


def acc_logout(request):
    logout(request)
    return redirect("/crm/")
