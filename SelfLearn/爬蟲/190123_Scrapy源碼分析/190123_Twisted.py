from twisted.internet import reactor    # 事件循環(可理解為select+while)，終止條件:所有socket皆移除
from twisted.web.client import getPage  # 創建Socket對象(如果下載完成會自動從事件循環中移除)
from twisted.internet import defer      # defer.Deferred => 特殊的Socket對象(不會發請求，故需手動移除)


# """2.將socket添加到事件循環中(加上@defer.inlineCallbacks裝飾器，並yield socket對象)"""
# def response(content):
#     print(content)
#
# @defer.inlineCallbacks
# def task():
#     url = "https://www.baidu.com"
#     """1.利用getPage創建socket"""
#     d = getPage(url.encode("utf-8"))
#     # 添加回調函數
#     d.addCallback(response)
#     yield d
#     url = "https://www.google.com"
#     """1.利用getPage創建socket"""
#     d = getPage(url.encode("utf-8"))
#     # 添加回調函數
#     d.addCallback(response)
#     yield d
#
# # d = task()  # d為yield返回值，也就是socket對象
#
# """4.監聽socket，並設定當請求完成時移除"""
# def done(*args, **kwargs):
#     reactor.stop()
#
# li = []
# for i in range(2):
#     d = task()  # d為yield返回值，也就是socket對象
#     li.append(d)
#
# dd = defer.DeferredList(li)  # 監聽
# dd.addBoth(done)  # addBoth() => 當事件完成(addCallback)或失敗(addErrback)時調用
#
# """3.開始事件循環(內部發送請求，並接收響應，當所有socket請求完成後，終止事件循環)"""
# reactor.run()


"""2.將socket添加到事件循環中(加上@defer.inlineCallbacks裝飾器，並yield socket對象)"""
# 全局變量
_close = None
count = 0
def response(content):
    print(content)
    global count
    count += 1
    print(count)
    if count == 4:
        _close.callback(None)  # 手動終止_close(特殊的Socket對象)

@defer.inlineCallbacks
def task():
    # 每個爬蟲的開始: start_request
    url = "https://www.baidu.com"
    """1.利用getPage創建socket"""
    d1 = getPage(url.encode("utf-8"))
    d1.addCallback(response)  # 添加回調函數

    url = "https://www.google.com"
    """1.利用getPage創建socket"""
    d2 = getPage(url.encode("utf-8"))
    d2.addCallback(response)  # 添加回調函數
    global _close
    _close = defer.Deferred()
    yield _close

"""4.監聽socket，並設定當請求完成時移除"""
def done(*args, **kwargs):
    reactor.stop()

# 每一個爬蟲
d1 = task()  # d為yield返回值，也就是socket對象
d2 = task()

dd = defer.DeferredList([d1, d2])  # 監聽
dd.addBoth(done)  # addBoth() => 當事件完成(addCallback)或失敗(addErrback)時調用

"""3.開始事件循環(內部發送請求，並接收響應，當所有socket請求完成後，終止事件循環)"""
reactor.run()