from django.shortcuts import render, HttpResponse, redirect
import requests
import time
import re
import json


CTIME = None
QCODE = None
TIP = 1


def login(request):
    global CTIME, QCODE
    CTIME = time.time()
    response = requests.get(
        url="https://login.wx.qq.com/jslogin?appid=wx782c26e4c19acffb&fun=new&lang=zh_TW&_=%s" % CTIME
    )
    print("response", response.text)
    v = re.findall('uuid = "(.*)";', response.text)
    # print(v)
    QCODE = v[0]
    return render(request, "login.html", {"qcode": QCODE})


def check_login(request):
    global TIP
    ret = {"code": 408, "data": None}
    r1 = requests.get(
        url="https://login.wx.qq.com/cgi-bin/mmwebwx-bin/login?loginicon=true&uuid=%s&tip=%s&r=-1517428513&_=%s" % (QCODE, TIP, CTIME),
    )
    if "window.code=408" in r1.text:
        # 無人掃描
        return HttpResponse(json.dumps(ret))
    elif "window.code=201" in r1.text:
        # 掃了但還沒按登入
        TIP = 0
        ret["code"] = 201
        v = re.findall('window.userAvatar = "(.*)";', r1.text)
        # print(r1.text)
        if v:
            avatar = v[0]
        else:
            avatar = "https://res.cloudinary.com/teepublic/image/private/s--nT5_0X7l--/t_Preview/b_rgb:ffffff,c_limit,f_jpg,h_630,q_90,w_630/v1512053883/production/designs/2122665_1.jpg"
        ret["data"] = avatar
        print(ret)
        return HttpResponse(json.dumps(ret))
    elif "window.code=200" in r1.text:
        # 掃了且登入
        """
        window.code=200;
        window.redirect_uri="https://web.wechat.com/cgi-bin/mmwebwx-bin/webwxnewloginpage?ticket=Aj8v8s4NRrdTWYCzjAZchhZI@qrticket_0&uuid=AY0k8FZSrg==&lang=zh_TW&scan=1547708423";
        """
        ret["code"] = 200
        # print(r1.text)
        url = re.findall('window.redirect_uri="(.*)";', r1.text)[0]

        r2 = requests.get(
            url=url,
        )
        print(r2.text)
        return HttpResponse(json.dumps(ret))
    else:
        print("else", r1.text)
        return HttpResponse(json.dumps(ret))
