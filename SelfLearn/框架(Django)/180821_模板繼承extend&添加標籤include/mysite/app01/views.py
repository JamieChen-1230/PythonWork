from django.shortcuts import render, HttpResponse
import time, datetime
# Create your views here.


def base(request):
    # return render(request, "index.html")
    return render(request, "base.html")

def extends(request):
    student_list = ['jamie', 'sb', 'nb']
    return render(request, 'extends.html', locals())
