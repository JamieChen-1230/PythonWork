"""
事例一：
gevent + requests
"""
# import gevent
# import requests
# from gevent import monkey
#
# monkey.patch_all()  # 必須加
#
#
# def task(method, url, req_kwargs):
#     print(method, url, req_kwargs)
#     response = requests.request(method=method, url=url, **req_kwargs)
#     print(response.url, response.content)
#
# # ##### 发送请求 #####
# # gevent.joinall([
# #     gevent.spawn(task, method='get', url='https://www.python.org/', req_kwargs={}),
# #     gevent.spawn(task, method='get', url='https://www.google.com/', req_kwargs={}),
# #     gevent.spawn(task, method='get', url='https://github.com/', req_kwargs={}),
# # ])
#
# # ##### 发送请求（协程池控制最大协程数量） #####
# from gevent.pool import Pool
# # 協程池
# pool = Pool(3)
# gevent.joinall([
#     pool.spawn(task, method='get', url='https://www.python.org/', req_kwargs={}),
#     pool.spawn(task, method='get', url='https://www.yahoo.com/', req_kwargs={}),
#     pool.spawn(task, method='get', url='https://www.github.com/', req_kwargs={}),
# ])


"""
事例二：
gevent + requests = grequests
"""
import grequests


request_list = [
    grequests.get('https://www.yahoo.com/'),
    grequests.get('https://www.python.org/'),
    grequests.get('https://www.github.com/')
]


# ##### 执行并获取响应列表 #####
response_list = grequests.map(request_list, size=5)  # size為協程池大小
print(response_list)


# ##### 执行并获取响应列表（处理异常） #####
# def exception_handler(request, exception):
#     print(request, exception)
#     print("Request failed")
#
#
# response_list = grequests.map(request_list, exception_handler=exception_handler)
# print(response_list)
