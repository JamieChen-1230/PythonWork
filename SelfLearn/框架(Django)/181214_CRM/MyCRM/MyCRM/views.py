from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout


def acc_login(request):
    if request.method == "GET":
        return render(request, "login.html")
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
            next_url = request.GET.get("next", "/")  # .get("要取的key", "找不到時的默認值")
            return redirect(next_url)
        else:
            error_msg = "Wrong username or password"
            return render(request, "login.html", {"error_msg": error_msg})
        # ---------django自帶驗證登入---------


def acc_logout(request):
    logout(request)
    return redirect("/crm/")
