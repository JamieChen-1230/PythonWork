# ------跌代器------
# 跌代器協議：對象必須提供next()方法，執行此方法要嘛回傳下一項，要嘛回傳異常並終止跌代。(只能往後走不能往前)
# 可跌代對象：實現了跌代器協議的對象。
# 可使用for, sum, max等去訪問可跌代對象。
# 使用for去循環較好，因可以統一的方式去實現有序和無序數據類型，且使用跌代的話是調用時才會存進內存(較省內存)。

# *(重點) 本質上之前學的列表、元組、字典、字符串、集合與文件都不是可跌代對象，
# 只不過for循環會自動調用它們的__iter__()方法，讓它們變成了可跌代對象。
# name = "SB"
# iter_name = name.__iter__()  # 變成了可跌代對象，可調用__next__()方法
# print(iter_name)  # => <str_iterator object at 0x000001AC62392FD0>
# print(iter_name.__next__())  # => S
# print(iter_name.__next__())  # => B
# print(iter_name.__next__())  # => 報錯(異常發生)

# 跌代器方法(能實現有序和無序數據類型，EX：字典(無序))
# li = [1, 2, 3]
# for i in li:  # 裡面自動調用 iter_li = li.__iter__(),  iter_li.__next__()
#     print(i)
# 不使用跌代器方法(只能實現有序數據類型)
# i = 0
# while i < len(li):
#     print(li[i])
#     i += 1

# 無序數據類型跌代
# dic = {'a': 1, "b": 2, "c": 3}
# iter_dic = dic.__iter__()  # iter_dic = 也可用iter(dic)
# print(iter_dic.__next__())  # => b，默認是keys
# print(iter_dic.__next__())  # => c
# print(next(iter_dic))  # => a，也可使用next()方法調用

# ------生成器------(不需調用__iter__()，本身就是可跌代對象)
# 語法上跟函數類似，差別在於使用yield返回值並保存當前狀態。
# 自動實現跌代器協議。
# ------生成器函數------
# def test():
#     yield 1  # 也是回傳值，但不像return只能使用一次
#     yield 2
#     yield 3
# g = test()
# print(g)  # => <generator object test at 0x000001DBC29FEF68>，生成器
# print(g.__next__())  # => 1
# print(g.__next__())  # => 2
# print(g.__next__())  # => 3

# def birth():
#     print("開始生")
#     yield "自己"    #  yield會保持函數運行狀態
#     print("繼續生")
#     yield "兒子"
# res = birth()  # 不會執行print("開始生")，直到使用next()後才開始執行
# import time
# time.sleep(1)
# print(next(res))  # => 自己，停在 yield "自己"
# time.sleep(1)
# print(next(res))  # => 兒子，停在 yield "兒子"

# ------列表解析&生成器表達式------
# 三元表達式
# name = "jamie"
# res = "SB" if name == "jamie" else '帥哥'
# print(res)  # => SB

# 一般列表
# li = []
# for i in range(10):
#     li.append("雞蛋%s" % i)
# print(li)  # => ['雞蛋0', '雞蛋1', '雞蛋2', '雞蛋3', '雞蛋4', '雞蛋5', '雞蛋6', '雞蛋7', '雞蛋8', '雞蛋9']

# 列表解析(二元表達式)
# li = ["雞蛋%s" % i for i in range(10)]
# print(li)  # => ['雞蛋0', '雞蛋1', '雞蛋2', '雞蛋3', '雞蛋4', '雞蛋5', '雞蛋6', '雞蛋7', '雞蛋8', '雞蛋9']
# print(type(li))  # => <class 'list'>

# 列表解析(三元表達式)
# li = ["雞蛋%s" % i for i in range(10) if i > 5]
# print(li)  # => ['雞蛋6', '雞蛋7', '雞蛋8', '雞蛋9']
# print(type(li))  # => <class 'list'>
# # error = ["雞蛋%s" % i for i in range(10) if i > 5 else i]  # 報錯，因不可四元(只能小於等於三元)

# 生成器表達式
# li = ("雞蛋%s" % i for i in range(10))  # => 使用小括號()
# print(li)  # => <generator object <genexpr> at 0x000002606399EF68>
# for i in li:  # for循環可執行可跌代對象
#     print(i)

# yield 相當於return，控制的是函式返回值
# x = yeild 則是會接收send()的值並賦予給yeild
# def test():
#     print("一")  # => 一
#     x = yield 1
#     print("二", x)  # => 二 傳值給yield
#     yield 2
# import time
# res = test()
# time.sleep(1)
# print(res.__next__())  # => 1
# time.sleep(1)
# # print(res.__next__())  # => 1
# print(res.send('傳值給yield'))  # => 2，傳值給yield讓x能接到值，並繼續執行到下個yield(相當於執行一個next())

# 跌代器只能使用一次
# li = (i for i in range(5))
# for i in li:
#     print(i, end='')  # => 01234
# for i in li:
#     print(i)   # =>  ，啥都沒有(因為上個for已經把跌代器都循環過了一遍)
# 本質上不是跌代器則沒有此問題
# li = [1, 2, 3, 4, 5]
# for i in li:
#     print(i, end='')  # => 12345
# for i in li:
#     print(i, end='')   # => 12345，因為列表本質上不是跌代器，只是for幫他轉為可跌代對象而已

# ------生產者消費者模型------
# import time
# times = 0
# def consumer(i):
#     global times
#     print('我是%s，我要吃包子了' % i)
#     while True:
#         food = yield
#         times += 1
#         time.sleep(0.1)
#         print("我是%s，我把%s吃掉了【%s】" % (i, food, times))
#
# def producer(names):
#     for n in range(len(names)):
#         c = consumer(names[n])
#         c.__next__()
#         for i in range(n*10, (n+1)*10):
#             time.sleep(0.1)
#             c.send("包子%s" % i)
#         time.sleep(1)
# producer(['jamie', 'sb'])
