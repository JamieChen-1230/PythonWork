class Mypagination(object):
    """
    自定義分頁類
    """
    def __init__(self, totalCount, currentPage, perPageItemNum=30, maxPageNum=7):
        """
        :param totalCount: 數據總個數
        :param currentPage: 當前頁
        :param perPageItemNum: 每頁數據數
        :param maxPageNum: 最多顯示頁碼數
        """
        # 數據總個數
        self.totalCount = totalCount
        # 當前頁
        try:
            self.currentPage = int(currentPage)
            if self.currentPage <= 0:
                self.currentPage = 1
        except Exception as e:
            self.currentPage = 1
        # 每頁數據數
        self.perPageItemNum = perPageItemNum
        # 最多顯示頁碼數
        self.maxPageNum = maxPageNum

    def start(self):
        """
        :return: 項目切片起始值
        """
        return (self.currentPage - 1) * self.perPageItemNum

    def end(self):
        """
        :return: 項目切片結尾值
        """
        return self.currentPage * self.perPageItemNum

    @property  # 靜態屬性，加上這個之後調用方法就不用加()
    def num_pages(self):
        """
        :return: 總頁數
        """
        # divmod()得出商和餘
        x, y = divmod(self.totalCount, self.perPageItemNum)
        if y == 0:
            return x
        else:
            return x + 1

    def page_num_range(self):
        """
        判斷頁碼條的顯示頁碼為何
        :return: 頁碼
        """
        if self.num_pages < self.maxPageNum:
            # 總頁數太少
            return range(1, self.num_pages + 1)
        elif self.currentPage <= int(self.maxPageNum / 2):
            # 前面幾頁不能顯示負數
            return range(1, self.maxPageNum + 1)
        elif self.currentPage + int(self.maxPageNum / 2) > self.num_pages:
            # 最後幾頁顯示不能超過總頁數
            return range(self.num_pages - self.maxPageNum + 1, self.num_pages + 1)
        else:
            # 其他前後頁數都夠的情況
            return range(self.currentPage - int(self.maxPageNum / 2),
                         self.currentPage + int(self.maxPageNum / 2) + 1)

    def page_str(self):
        """
        直接產生頁碼條的<a>，這樣就不用在html中使用迴圈
        :return: 頁碼條字符串
        """
        page_list = []
        # --------首頁--------
        first = "<li><a href='/my_pagination?p=%s'>首頁</a></li>" % 1
        page_list.append(first)

        # --------上一頁--------
        if self.currentPage == 1:
            prev = "<li><a href='#'>上一頁</a></li>"
        else:
            prev = "<li><a href='/my_pagination?p=%s'>上一頁</a></li>" % (self.currentPage - 1)
        page_list.append(prev)

        # --------頁碼--------
        for i in self.page_num_range():
            if i == self.currentPage:
                temp = "<li class='active'><a href='/my_pagination?p=%s'>%s</a></li>" % (i, i)
            else:
                temp = "<li><a href='/my_pagination?p=%s'>%s</a></li>" % (i, i)
            page_list.append(temp)

        # --------下一頁--------
        if self.currentPage == self.num_pages:
            forward = "<li><a href='#'>下一頁</a></li>"
        else:
            forward = "<li><a href='/my_pagination?p=%s'>下一頁</a></li>" % (self.currentPage + 1)
        page_list.append(forward)

        # --------尾頁--------
        last = "<li><a href='/my_pagination?p=%s'>尾頁</a></li>" % self.num_pages
        page_list.append(last)

        return ''.join(page_list)
