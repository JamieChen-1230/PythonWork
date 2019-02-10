import requests


"""
方法關係: 
requests.request("get" ...) = requests.get(....)
有這些方法:
requests.get()
requests.post()
requests.delete()
requests.put()
requests.patch()
requests.options()
requests.head()
"""

"""
requests.request參數:
    - method: 提交方式
    - url: 提交地址
    - params: 在url中傳遞的參數，適用於GET
        http://www.oldboyedu.com?k1=v1&k2=v2
        requests.request(
            method="GET",
            url="http://www.oldboyedu.com",
            params={"k1": "v1", "k2": "v2", },
        )
    - data: 在請求體中傳遞的參數，參數value不可為字典型式
        requests.request(
            method="POST",
            url="http://www.oldboyedu.com",
            data={"k1": "v1", "k2": "v2", },
        )
        請求頭:
            content-type: application/x-www-form-urlencoded
        請求體:
            k1=v1&k2=v2
    - json: 在請求體中傳遞的參數(以json格式傳遞)，參數value可為字典型式
        requests.request(
            method="POST",
            url="http://www.oldboyedu.com",
            json={"k1": "v1", "k2": "v2", },
        )
        請求頭:
            content-type: application/json....
        請求體:
            "{"k1": "v1", "k2": "v2"}"
    - headers: 請求頭(有些網站會用這些來判斷是否為合理訪問)
        requests.request(
            method="POST",
            url="http://www.oldboyedu.com",
            data={"k1": "v1", "k2": "v2", },
            headers={
                # 從哪個網站來的
                "referer": "https://dig.chouti.com/",
                # 使用的是哪個瀏覽器
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36"
            }
        )
    - cookies: Cookies
    - files: 上傳文件
        requests.request(
            method="POST",
            url="http://www.oldboyedu.com"
            files={
                "f1": open("test.py", "rb"),
                "f2": ("新的文件名", open("test.py", "rb")),
            }
        )
    - timeout: 等待服務器回應的時間限制
    - allow_redirects: 是否允許重定向
    - proxies: 代理發送請求，用來躲過IP被封鎖
        requests.request(
            method="GET",
            url="http://www.oldboyedu.com",
            proxies={
                "http": "http://4.19.128.5: 9000",
            }
        )
    - stream: 是否可以分段操作
    - cert: 主動提出證書文件
        requests.request(
            method="GET",
            url="https://www.oldboyedu.com",
            cert="test123.pem",
        )
    - verify: 是否驗證證書，一般https網站透過verify=False就可以了
"""
