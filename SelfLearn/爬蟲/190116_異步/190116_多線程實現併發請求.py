"""
可以實現併發，但請求發送出去到回來之前的中間這段時間都在等待沒利用到。
編寫方式:
    一、 直接返回處理
    二、 通過回調函數分工處理
"""
# --------------方式一--------------

from concurrent.futures import ThreadPoolExecutor
import requests

# 創建線程池
pool = ThreadPoolExecutor(6)

url_list = [
    "http://www.cnblogs.com/wupeiqi",
    "http://www.bing.com",
    "http://www.zhihu.com",
    "http://www.sina.com",
    "http://www.baidu.com",
    "http://www.autohome.com.cn",
]

def task(url):
    response = requests.get(url=url)
    print(url, response)

for url in url_list:
    pool.submit(task, url)

pool.shutdown(wait=True)


# --------------方式二--------------
# 跟方法一的差別在於把工作拆成不同函數執行，函數間的耦合較低，維護較容易
"""
from concurrent.futures import ThreadPoolExecutor
import requests


# 創建線程池
pool = ThreadPoolExecutor(6)

url_list = [
    "http://www.cnblogs.com/wupeiqi",
    "http://www.bing.com",
    "http://www.zhihu.com",
    "http://www.sina.com",
    "http://www.baidu.com",
    "http://www.autohome.com.cn",
]


def task(url):
    # 下載頁面
    response = requests.get(url=url)
    # print(url, response)
    return response


def done(future, *args, **kwargs):
    response = future.result()  # future.result()回傳的是前一個函數的返回值
    print(response.status_code, response.content)


for url in url_list:
    v = pool.submit(task, url)
    v.add_done_callback(done)  # 回調函數，當下載頁面結束後執行done()

pool.shutdown(wait=True)
"""