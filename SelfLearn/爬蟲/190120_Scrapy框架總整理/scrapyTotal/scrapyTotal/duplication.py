
class MyFilter(object):

    def __init__(self):  # 2. 對象初始化
        self.visited_set = set()

    # -------這些方法是必須要有的且不能改名稱-------
    @classmethod
    def from_settings(cls, settings):  # 1. 創建對象
        """
        obj = MyFilter.from_settings()
        """
        return cls()

    def request_seen(self, request):  # 4.檢查
        """檢測當前url是否存在"""
        if request.url in self.visited_set:
            return True
        self.visited_set.add(request.url)
        return False

    def open(self):  # can return deferred  # 3.開始爬取
        print("FilterOn")
        pass

    def close(self, reason):  # can return a deferred # 5.結束爬取
        print("FilterClose")
        pass

    def log(self, request, spider):  # log that a request has been filtered
        pass
    # -------這些方法是必須要有的且不能改名稱-------
