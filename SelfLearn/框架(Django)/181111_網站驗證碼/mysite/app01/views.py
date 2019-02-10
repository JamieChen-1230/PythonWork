from django.shortcuts import render, HttpResponse
from utils.check_code import create_validate_code
from io import BytesIO


def register(request):
    if request.method == "GET":
        return render(request, "register.html")
    elif request.method == "POST":
        input_code = request.POST.get("code")
        check_code = request.session["check_code"]
        print(input_code, check_code)
        return HttpResponse("...")


def verification(request):
    # BytesIO對象: 在內存中讀寫，可讀寫bytes
    # StringIO對象: 在內存中讀寫，可讀寫字串
    f = BytesIO()
    # 返回驗證碼圖片對象和驗證碼
    img, code = create_validate_code()
    # 將驗證碼加入session，方便我們之後調用
    request.session["check_code"] = code
    print(code)
    # img.save() 要把圖片寫到哪個文件裡
    img.save(f, "PNG")

    # f.getvalue() 把文件中的所有值取出
    return HttpResponse(f.getvalue())

