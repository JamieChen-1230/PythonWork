from django.shortcuts import render, HttpResponse
import json, os


def ajax(request):
    return render(request, 'ajax.html', locals())


def receive(request):
    print(request.GET)
    print(request.POST)
    print(request.body)
    ret = {'status': True, 'message': 'Okkkkk'}

    return HttpResponse(json.dumps(ret))


def files_receive(request):
    print(request.GET)
    print(request.POST)
    print(request.FILES)
    ret = {'status': True, 'message': 'Okkkkk'}
    import json
    return HttpResponse(json.dumps(ret))


def iframe_example(request):
    return render(request, 'iframe_example.html')


def receive_example(request):
    print(request.FILES)

    ret = {'status': True, "data": None, 'message': None}
    obj = request.FILES.get('img')

    file_path = os.path.join('static', obj.name)
    f = open(file_path, 'wb')
    for line in obj.chunks():
        f.write(line)
    f.close()

    ret['data'] = file_path
    return HttpResponse(json.dumps(ret))
