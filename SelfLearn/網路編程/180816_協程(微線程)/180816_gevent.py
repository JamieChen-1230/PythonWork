import gevent
import requests, time

start = time.time()
def f(url):
    print('GET: %s' % url)
    resp = requests.get(url)
    data = resp.text
    print('%d bytes received from %s.' % (len(data), url))

gevent.joinall([
        gevent.spawn(f, 'https://www.python.org/'),
        gevent.spawn(f, 'https://www.yahoo.com/'),
        gevent.spawn(f, 'https://www.baidu.com/'),
        gevent.spawn(f, 'https://www.sina.com.cn/'),
        gevent.spawn(f, 'https://www.shutterstock.com/zh-Hant/?kw=%E5%9C%96%E7%89%87%E7%B6%B2&gclid=CjwKCAjwns_bBRBCEiwA7AVGHgOFKysvqrS3J0LpMrBZO55bdmJ1J76UMpRMNiTk30BKusYLjZcIIhoCv3cQAvD_BwE&gclsrc=aw.ds&dclid=CLPwmJX-8NwCFcFplgodfTEKjw'),
])

# f('https://www.python.org/')
# f('https://www.yahoo.com/')
# f('https://www.baidu.com/')
# f('https://www.sina.com.cn/')
# f('https://www.shutterstock.com/zh-Hant/?kw=%E5%9C%96%E7%89%87%E7%B6%B2&gclid=CjwKCAjwns_bBRBCEiwA7AVGHgOFKysvqrS3J0LpMrBZO55bdmJ1J76UMpRMNiTk30BKusYLjZcIIhoCv3cQAvD_BwE&gclsrc=aw.ds&dclid=CLPwmJX-8NwCFcFplgodfTEKjw')

print("cost time:", time.time()-start)
