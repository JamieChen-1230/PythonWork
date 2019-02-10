from django.shortcuts import render, HttpResponse
from django import forms
from django.forms import fields


class Uploadform(forms.Form):
    user = fields.CharField()
    img = fields.FileField()


def upload_forms(request):
    if request.method == "GET":
        return render(request, 'upload_forms.html', locals())
    else:
        obj = Uploadform(request.POST, request.FILES)
        if obj.is_valid():
            user = obj.cleaned_data.get('user')
            img = obj.cleaned_data.get('img')

            f = open(img.name, 'wb')
            # 文件內容是分段上傳，所以需用迴圈處理
            for line in img.chunks():
                f.write(line)
            f.close()
            return HttpResponse('ok')


def upload(request):
    if request.method == "GET":
        return render(request, 'upload.html', locals())
    else:
        print(request.POST)
        print(request.FILES)
        user = request.POST.get('user')
        img = request.FILES.get('img')
        # img為一對象，包含文件大小、名稱、內容等
        print(img.name)
        print(img.size)
        
        f = open(img.name, 'wb')
        # 文件內容是分段上傳，所以需用迴圈處理
        for line in img.chunks():
            f.write(line)
        f.close()

        return HttpResponse('ok')
