# 函數即變量
# 不修改變數

# 1.高階函數定義：傳入參數是函數名或者回傳值是函數名
# def foo(n):
#     print(n)
# def bar(name):
#     print("I am %s" % name)
#
# foo(bar)  # => bar()內存位置，高階函數(傳入參數式函數)
# foo(bar("jamie"))  # => None

# def bar():
#     print("from bar")
# def hanle():
#     print("from hanle")
#     return bar()   # 高階函數(回傳值是函數)
# print(hanle())  # => None，bar()回傳None

# 2.尾調用優化(在最後一步才調用另一個函數)，讓程序不用保存上一層狀態以省內存
# def a():
#     print("a")
# def b():
#     print("b")
#     return a()  # 尾調用
# b()

# def a():
#     print("a")
# def b():
#     print("b")
#     return a()  # 非尾調用
#     print("bb")
# b()

# def a():
#     print("a")
#     return "a"
# def b():
#     print("b")
#     return a() + "1"  # 非尾調用(因為還要等回傳然後+"1")
# print(b())


# 3.map函數(處理序列中的每個元素，輸出為一個元素個數和位置與原來相同的列表)
# 自己設的map函數
# num_1 = [1, 2, 10, 5, 3, 7]
# def map_test(func, array):
#     res = []
#     for i in array:
#         i = func(i)
#         res.append(i)
#     return res
# print(map_test(lambda x: x**2, num_1))  # => [1, 4, 100, 25, 9, 49]

# Python內建map函數(map為可跌代對象)
# num_1 = [1, 2, 10, 5, 3, 7]
# res = map(lambda x: x**2, num_1)  # 參數一為函數，二為一個可跌代對象(字符串、列表、元組、字典)
# print(res, type(res))  # => <map object at 0x000001E11255A978> <class 'map'>，map為可跌代對象
# print(list(res))  # => [1, 4, 100, 25, 9, 49]


# 4.filter函數(判斷序列中的每個元素得到布林值，如果是True留下)
# 自己設的filter函數
# people = ["jamie", "sb_jamie", "sb_alex"]
# def remove_sb(n):
#     return n.startswith("sb")
# def filter_test(func, array):
#     res = []
#     for i in array:
#         if func(i):
#             res.append(i)
#     return res
# print(filter_test(remove_sb, people))  # => ['sb_jamie', 'sb_alex']

# Python內建filter函數(filter為可跌代對象)
# people = ["jamie", "sb_jamie", "sb_alex"]
# res = filter(lambda x: not x.startswith("sb"), people)  # 參數一為函數，二為一個可跌代對象(字符串、列表、元組、字典)
# print(res, type(res))  # => <filter object at 0x000001E3DD5F9CF8> <class 'filter'>
# print(list(res))  # => ['jamie']
# print(list(filter(lambda x: x.startswith("sb"), people)))  # => ['sb_jamie', 'sb_alex']
# # print(next(res))

# 5.reduce函數(處裡一個序列，然後進行合併操作)
# 自己設的reduce函數
# num_1 = [1, 2, 3, 100]
# def reduce_test(func, array, init = None):
#     if init == None:
#         res = array.pop(0)
#     else:
#         res = init
#     for i in array:
#         res = func(res, i)
#     return res
# print(reduce_test(lambda x, y: x*y, num_1))  # => 600

# Python內建reduce函數
# from functools import reduce
# num_1 = [1, 2, 3, 100]
# res = reduce(lambda x, y: x*y, num_1, 1)
# print(res, type(res))  # => 600 <class 'int'>

