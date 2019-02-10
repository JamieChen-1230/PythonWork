import json
from io import BytesIO
from django.shortcuts import HttpResponse
from django.shortcuts import render
from django.shortcuts import redirect
from repository import models
from utils.check_code import create_validate_code
from web.forms.account import LoginForm, RegisterForm
from datetime import datetime
from utils.pagination import Pagination
from backend.auth.auth import check_login


def login(request):
    """
    登入
    :param request:
    :return:
    """
    if request.method == "GET":
        obj = LoginForm(request)
        return render(request, "login.html", locals())
    else:
        result = {'status': False, 'message': None, 'data': None}
        obj = LoginForm(request, request.POST)
        if obj.is_valid():
            print(obj.cleaned_data)
            username = obj.cleaned_data.get("username")
            password = obj.cleaned_data.get("password")
            user_info = models.UserInfo.objects.filter(username=username, password=password).values('nid',
                                                                                                    'nickname',
                                                                                                    'username', 'email',
                                                                                                    'avatar',
                                                                                                    'blog__nid',
                                                                                                    'blog__site').first()
            if user_info:
                request.session["user_info"] = user_info
                print(request.session["user_info"])
                result["data"] = user_info
                result["status"] = True
                return redirect("/")
            else:
                result["message"] = "帳號密碼錯誤"
                obj.errors["username"] = ("帳號密碼錯誤",)
                return render(request, "login.html", locals())
        else:
            print(obj.errors)
            result["message"] = obj.errors
            return render(request, "login.html", locals())


def register(request):
    """
    註冊
    :param request:
    :return:
    """
    if request.method == "GET":
        obj = RegisterForm(request)
        return render(request, "register.html", locals())
    else:
        result = {'status': False, 'message': None, 'data': None}
        obj = RegisterForm(request, request.POST)
        if obj.is_valid():
            data = obj.cleaned_data
            del data["check_code"]
            del data["password_ck"]
            print(data)
            models.UserInfo.objects.create(**data)
            return redirect("/")
        else:
            print(obj.errors)
            return render(request, "register.html", locals())


def logout(request):
    """
    登出
    :param request:
    :return:
    """
    request.session.clear()
    return redirect('/')


def check_code(request):
    """
    驗證碼
    :param request:
    :return:
    """
    # BytesIO對象: 在內存中讀寫，可讀寫bytes
    f = BytesIO()
    # 得出驗證碼對象和字串
    img, code = create_validate_code()
    # 透過save()把圖形寫進文件
    img.save(f, 'PNG')
    # 將驗證碼加入session，方便我們之後調用
    request.session['check_code'] = code
    # getvalue()會把文件的所有值拿出來
    return HttpResponse(f.getvalue())


def receive_content(request):
    """
    提交評論
    :param request:
    :return:
    """
    print(request.POST.get("content"))
    print(request.session["user_info"].get("nid"))
    ret = {"status": False, "data": None}
    content = request.POST.get("content")
    article_id = request.POST.get("article_id")
    user_id = request.session["user_info"].get("nid")

    if content and article_id and user_id:
        obj = models.Comment.objects.create(content=content, article_id=article_id, user_id=user_id)
        ret["status"] = True
        ret["data"] = {
            "nickname": obj.user.nickname,
            "create_time": obj.create_time,
            "content": content,
        }
    print(ret)
    return HttpResponse(json.dumps(ret, cls=ComplexEncoder))


# 因為日期格式無法直接被json序列化，故加上此
class ComplexEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.strftime('%Y-%m-%d %H:%M:%S')
        else:
            return json.JSONEncoder.default(self, obj)


@check_login
def updown(request):
    user_id = request.session["user_info"]["nid"]
    article_id = request.GET.get("article_id")
    dic = {
        "up": bool(request.GET.get("up")),
        "article_id": int(article_id),
        "user_id": user_id
    }
    # print(dic)
    ud_obj = models.UpDown.objects.filter(article_id=article_id, user_id=user_id).first()
    if ud_obj:
        models.UpDown.objects.filter(article_id=article_id, user_id=user_id).update(**dic)
    else:
        models.UpDown.objects.create(**dic)

    up_count = models.UpDown.objects.filter(article_id=article_id, up=True).count()
    # print(up_count)
    down_count = models.UpDown.objects.filter(article_id=article_id, up=False).count()
    # print(down_count)
    models.Article.objects.filter(nid=article_id).update(up_count=up_count, down_count=down_count)
    url = request.GET.get("url")
    print(request.GET.get("url"))
    return redirect(url)
