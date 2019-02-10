from django.shortcuts import render, HttpResponse
from django.views import View


def fbv(requset):
    if requset.method == 'GET':
        return HttpResponse('FBV.GET')
    elif requset.method == 'POST':
        return HttpResponse('FBV.POST')


# 'get', 'post', 'put', 'patch', 'delete', 'head', 'options', 'trace'
class Cbv(View):
    # 所有請求過來都會先經dispatch，dispatch在分配到哪個方法
    def dispatch(self, request, *args, **kwargs):
        ret = super(Cbv, self).dispatch(request, *args, **kwargs)  # 調用父類dispatch
        return ret

    # 如果用戶使用get發送請求，就會觸發get方法
    def get(self, request):
        ret = HttpResponse('CBV.GET')
        ret['h1'] = 'v1'
        ret.set_cookie('c1', 'v2')
        '''
        響應頭：
            h1=v1
            cookies: c1=v2
        響應體：
            CBV.GET
        '''
        return ret

    # 如果用戶使用post發送請求，就會觸發post方法
    def post(self, request):
        return HttpResponse('CBV.POST')
