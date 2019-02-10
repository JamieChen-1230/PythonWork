"""
asyncio初試:
一個線程實現併發(遇到IO阻塞時執行另一個程序)
"""
# import asyncio
#
# @asyncio.coroutine
# def task():
#     print('before...task......')
#     yield from asyncio.sleep(5)
#     print('end...task......')
#
#
# tasks = [task(), task()]
#
# loop = asyncio.get_event_loop()
# loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()


"""
事例一：
asyncio
因為asyncio不支持Http請求，但支持TCP請求，所以可以透過TCP請求發起Http請求
"""
# import asyncio
#
#
# @asyncio.coroutine
# def task(host, url='/'):
#     print("start", host, url)
#     reader, writer = yield from asyncio.open_connection(host, 80)  # 創建連結
#
#     request_header_content = """GET %s HTTP/1.0\r\nHost: %s\r\n\r\n""" % (url, host,)  # 發起Http請求
#     request_header_content = bytes(request_header_content, encoding='utf-8')
#
#     writer.write(request_header_content)
#     yield from writer.drain()
#     text = yield from reader.read()
#     print("end", host, url, text)
#     writer.close()
#
#
# tasks = [
#     task('www.cnblogs.com', '/wupeiqi/'),
#     task('dig.chouti.com', '/pic/show?nid=4073644713430508&lid=10273091'),
# ]
#
# loop = asyncio.get_event_loop()
# results = loop.run_until_complete(asyncio.gather(*tasks))
# loop.close()


"""
事例二： 
asyncio + aiohttp
因為asyncio不支持Http請求，所以使用aiohttp模塊來封裝Http請求數據包
"""
# import aiohttp
# import asyncio
#
#
# @asyncio.coroutine
# def task(url):
#     print(url)
#     response = yield from aiohttp.request('GET', url)
#     # data = yield from response.read()
#     # print(url, data)
#     print(url, response)
#     response.close()
#
#
# tasks = [task('http://www.google.com/'), task('https://www.baidu.com/')]
#
# event_loop = asyncio.get_event_loop()
# results = event_loop.run_until_complete(asyncio.gather(*tasks))
# event_loop.close()


"""
事例三： 
asyncio + requests
因為asyncio不支持Http請求，所以使用requests模塊來封裝Http請求數據包
"""
import asyncio
import requests


@asyncio.coroutine
def task(func, *args):
    print(func, args)
    loop = asyncio.get_event_loop()
    future = loop.run_in_executor(None, func, *args)  # requests.get(url)
    response = yield from future
    print(response.url, response.content)


tasks = [
    task(requests.get, 'http://www.cnblogs.com/wupeiqi/'),
    task(requests.get, 'http://dig.chouti.com/pic/show?nid=4073644713430508&lid=10273091')
]

loop = asyncio.get_event_loop()
results = loop.run_until_complete(asyncio.gather(*tasks))
loop.close()
