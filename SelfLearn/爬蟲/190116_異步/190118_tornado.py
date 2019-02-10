from tornado.httpclient import AsyncHTTPClient
from tornado.httpclient import HTTPRequest
from tornado import ioloop


COUNT = 0


def handle_response(response):
    """
    处理返回值内容（需要维护计数器，来停止IO循环），调用 ioloop.IOLoop.current().stop()
    :param response:
    :return:
    """
    global COUNT
    COUNT -= 1

    if response.error:
        print("Error:", response.error)
    else:
        print(response.body)

    if COUNT == 0:
        ioloop.IOLoop.current().stop()


def func():
    url_list = [
        'http://www.baidu.com',
        'http://www.google.com',
    ]

    global COUNT
    COUNT = (len(url_list))

    for url in url_list:
        print(url)
        http_client = AsyncHTTPClient()
        http_client.fetch(HTTPRequest(url), handle_response)  # handle_response為回調函數


ioloop.IOLoop.current().add_callback(func)
ioloop.IOLoop.current().start()  # 死循環
