# Python內置了一個WSGI服務器，這個模塊叫wsgiref
from wsgiref.simple_server import make_server  # 會幫我們做HTTP解析
import time

def jamie(environ):
    f = open("index1.html", "rb")
    data = f.read()
    f.close()
    return data

def login(environ):
    print(environ["QUERY_STRING"])
    f = open("login.html", "rb")
    data = f.read()
    f.close()
    return data

def show_time(environ):
    t = time.ctime()
    # return ('<h1>Time: %s</h1>' % t).encode('utf-8')
    f = open("show_time.html", "r", encoding="utf-8")
    data = f.read()
    f.close()
    data = data.replace("{{time}}", str(t))  # Low方法

    return data.encode('utf-8')

def router():
    url_patterns=[
        ("/login", login, ),
        ("/show_time", show_time,),
        ("/jamie", jamie, )
    ]
    return url_patterns

# application()函數就是符合WSGI標準的一個HTTP處理函數，它接收兩個參數：
# environ：一個包含所有HTTP請求信息的dict對象
# start_response：一個發送HTTP響應的函數
def application(environ, start_response):
    # print(environ)  # 這是服務器幫我們封裝好的請求信息(字典形式)
    # print(environ['PATH_INFO'])
    path = environ['PATH_INFO']
    start_response('200 OK', [('Content-Type', 'text/html')])  # 響應頭

    url_patterns = router()
    func=None
    for i in url_patterns:
        if path == i[0]:
            func = i[1]
            break
    if func:
        return [func(environ)]
    else:
        return [b'404']

    # 用if_else實現，效率差
    # if path == '/':
    #     return [b'<h1>Hello, web!</h1>']  # 真正要返回的頁面(字節形式)
    # elif path == '/jamie':
    #     return [jamie()]
    # else:
    #     return [b'<h1>404</h1>']

httpd = make_server('', 8000, application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()  # 監聽HTTP請求，有客戶端連接就會執行make_server('', 8000, application)裡的第三參數
