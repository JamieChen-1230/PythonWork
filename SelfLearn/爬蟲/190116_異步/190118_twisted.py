from twisted.web.client import getPage, defer
from twisted.internet import reactor


def all_done(arg):
    reactor.stop()


def one_done(contents):
    print(contents)


deferred_list = []

url_list = ['http://www.bing.com', 'http://www.baidu.com', ]
for url in url_list:
    deferred = getPage(bytes(url, encoding='utf8'))
    deferred.addCallback(one_done)
    deferred_list.append(deferred)

dlist = defer.DeferredList(deferred_list)
dlist.addBoth(all_done)
reactor.run()  # 開始循環，每一個回來都會執行one_done()，當所有都回來後執行all_dine()
