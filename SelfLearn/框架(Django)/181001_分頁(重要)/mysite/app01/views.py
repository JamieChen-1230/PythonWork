from django.shortcuts import render
# 引入分頁模塊
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

# 資料集
USER_LIST = []
for i in range(1, 999):
    temp = {'name': 'root' + str(i), 'age': i}
    USER_LIST.append(temp)


# ----------分頁基礎知識----------
def basis_pagination(request):
    per_page_count = 10
    current_page = request.GET.get('p')
    current_page = int(current_page)

    # p=1  =>  0-9項  =>  0,10
    # p=2  =>  10-19項  =>  10,20
    # ...
    start = (current_page - 1) * per_page_count
    end = current_page * per_page_count
    user_list = USER_LIST[start:end]

    prev_pager = current_page - 1
    next_pager = current_page + 1
    return render(request, 'basis_pagination.html', locals())


# ----------Django內置分頁----------
def internal_pagination(request):
    # 全部數據：USER_LIST  =>  總共多少數據
    # 每頁數據量：10
    paginator = Paginator(USER_LIST, 10)
    # paginator對象方法：
    # per_page:     每頁顯示條目數量
    # count:        數據總個數
    # num_pages:    總頁數
    # page_range:   總頁數的索引範圍(頁碼範圍)，如: (1,10),(1,200)
    # page:page     對象 (包含是否有上\下一頁等)

    current_page = request.GET.get('p')
    try:
        posts = paginator.page(current_page)
        # paginator.page對象方法：
        # has_next:              是否有下一頁
        # next_page_number:      下一頁頁碼
        # has_previous:          是否有上一頁
        # previous_page_number:  上一頁頁碼
        # object_list:           分頁之後的數據列表，已經做好切片了
        # number:                當前頁
        # paginator:             paginator對象
    except PageNotAnInteger:  # 若頁數不是整數，默認到第一頁
        posts = paginator.page(1)
    except EmptyPage:  # 若空頁，默認到最後一頁
        posts = paginator.page(paginator.num_pages)

    return render(request, 'internal_pagination.html', locals())


# ----------擴展Paginator模塊----------
class ExtendPaginator(Paginator):
    def __init__(self, current_page, per_page_number, *args, **kwargs):
        self.current_page = int(current_page)  # 當前頁
        self.per_page_number = int(per_page_number)  # 最多顯示頁碼數量
        super(ExtendPaginator, self).__init__(*args, **kwargs)

    # 擴展方法
    def page_num_range(self):
        # self.current_page     當前頁
        # self.per_page_number  最多顯示頁碼數量
        # self.num_pages        總頁數
        if self.num_pages < self.per_page_number:
            # 總頁數太少
            return range(1, self.num_pages+1)
        elif self.current_page <= int(self.per_page_number/2):
            # 前面幾頁不能顯示負數
            return range(1, self.per_page_number+1)
        elif self.current_page+int(self.per_page_number/2) > self.num_pages:
            # 最後幾頁顯示不能超過總頁數
            return range(self.num_pages-self.per_page_number+1, self.num_pages+1)
        else:
            # 其他前後頁數都夠的情況
            return range(self.current_page-int(self.per_page_number/2),
                         self.current_page+int(self.per_page_number/2)+1)


# ----------擴展Django內置分頁----------
def extend_pagination(request):
    current_page = request.GET.get('p')

    # 全部數據：USER_LIST  =>  總共多少數據
    # 每頁數據量：10
    paginator = ExtendPaginator(current_page, 11, USER_LIST, 10)

    try:
        posts = paginator.page(current_page)
    except PageNotAnInteger:  # 若頁數不是整數，默認到第一頁
        posts = paginator.page(1)
    except EmptyPage:  # 若空頁，默認到最後一頁
        posts = paginator.page(paginator.num_pages)

    return render(request, 'extend_pagination.html', locals())


# ----------自定義分頁組件----------
def my_pagination(request):
    from app01.mypager import Mypagination
    current_page = request.GET.get('p')

    page_obj = Mypagination(999, current_page)

    data_list = USER_LIST[page_obj.start(): page_obj.end()]
    return render(request, 'my_pagination.html', locals())
