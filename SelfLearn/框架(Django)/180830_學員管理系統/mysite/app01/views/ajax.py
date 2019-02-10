from django.shortcuts import render, HttpResponse


def ajax_start(request):
    return render(request, 'ajax_start.html')


def ajax_submit(request):
    user = request.GET.get('user')
    pwd = request.GET.get('pwd')
    import time
    time.sleep(3)
    return HttpResponse(user)


def ajax_add(request):
    v1 = request.POST.get("v1")
    v2 = request.POST.get("v2")
    try:
        v3 = int(v1) + int(v2)
    except Exception as e:
        v3 = "格式錯誤"

    return HttpResponse(v3)
