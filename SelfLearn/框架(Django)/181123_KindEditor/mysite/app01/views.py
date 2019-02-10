from django.shortcuts import render, HttpResponse
import json


def editor(request):
    return render(request, "editor.html")


def receive(request):
    print(request.POST)
    print(request.FILES)
    
    img = request.FILES.get("imgFile")
    path = "static/imgs/" + img.name
    f = open(path, 'wb')
    # 文件內容是分段上傳，所以需用迴圈處理
    for line in img.chunks():
        f.write(line)
    f.close()
    
    # KindEditor 回覆格式
    ret = {
        "error": 0,
        "url": path,
        "message": "錯誤了"
    }
    return HttpResponse(json.dumps(ret))
