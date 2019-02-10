from django.shortcuts import render


def jsonp(request):
    return render(request, "jsonp.html")


def theory(request):
    return render(request, 'theory.html')