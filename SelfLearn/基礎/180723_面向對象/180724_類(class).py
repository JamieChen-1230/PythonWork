#  類 ：1.把一類事物的相同的特徵與動作整合到一起就是類。
#       2.類是一個抽象的概念(模具)
# 對象：就是基於類而創建的一個具體事物(具體存在的)
# 用面向對象編程獨有的語法class去實現面向對象設計
# 由類產生對象的過程叫做實例化(對象=實例)
# 類的屬性是共享的，但實例的屬性獨立的

# 基本介紹
# class Chinese:  # 類可以沒有括號，通常首字大寫
#     '這是一個中國人的類'
#     pass
# print(Chinese)  # => <class '__main__.Chinese'>，來自__main__(因直接執行檔)底下的Chinese類
# # 實例化
# p1 = Chinese()  # => <__main__.Chinese object at 0x000002855E472F60>，由__main__.Chinese產生的對象
# print(p1)


# 類的屬性：分為數據屬性(特徵)、函數屬性(方法)
# 類和對象都是經由點(.)來訪問屬性
# class Chinese:  # 類可以沒有括號，通常首字大寫
#     '這是一個中國人的類'
#     government = "共產黨"  # 數據屬性
#     # 函數屬性
#     def walk():
#         print("走路")
#     def sleep(self):
#         print("睡覺")
#
# print(Chinese.government)  # => 共產黨
# Chinese.walk()  # => 走路
# Chinese.sleep("參數")  # => 睡覺
# # print(dir(Chinese))  # 查看所有屬性
# # print(Chinese.__dict__)  # 查看類的屬性字典
# print(Chinese.__dict__['government'])  # => 共產黨
# Chinese.__dict__['walk']()  # => 走路
# Chinese.__dict__['sleep']("參數")  # => 睡覺


# 類的內建屬性介紹
# class Chinese:  # 類可以沒有括號，通常首字大寫
#     '這是一個中國人的類'
#     government = "共產黨"  # 數據屬性
#     def walk():
#         print("走路")
#     def sleep(self):
#         print("睡覺")
#
# print(Chinese.__name__)  # => Chinese
# print(Chinese.__doc__)  # => 這是一個中國人的類
# print(Chinese.__bases__)  # => (<class 'object'>,)，在python中所有的類都有一個祖先叫object
# print(Chinese.__module__)  # => __main__
# print(Chinese.__dict__)  # 查看類的屬性字典


# __init__，添加數據屬性到實例。實例能訪問類屬性但類不能訪問實例屬性
# class Chinese:  # 類可以沒有括號，通常首字大寫
#     '這是一個中國人的類'
#     government = "共產黨"  # 數據屬性
#     # self代表實例自己本身
#     def __init__(self, names, ages, genders):  # 調用實例化會自動執行__init__
#         # 自動把name,age,gender封裝到self裡並return
#         self.name = names  # 數據屬性
#         self.age = ages
#         self.gender = genders
#     def walk():
#         print("走路")
#     def sleep(self):
#         print("睡覺")
#
# # p1=Chinese("jamie", 20, "man") --> __init__(self, names, ages, genders) --> self=p1,names=jamie,ages=18,genders=man
# p1 = Chinese("jamie", 20, "man")  # 實例化
# print(p1)  # => <__main__.Chinese object at 0x00000156D6BF8908>
# print(p1.__dict__)  # => {'name': 'jamie', 'gender': 'man', 'age': 20}
# print(p1.name)  # => jamie
# print(p1.__dict__['name'])  # => jamie
# print(p1.government)  # => 共產黨，原因是因為在本身找不到但在上一層(class)找到了


# 添加函數屬性到實例。實例本身只有數據屬性沒有函數屬性，而是到類中去訪問的(省內存)
# class Chinese:  # 類可以沒有括號，通常首字大寫
#     '這是一個中國人的類'
#     government = "共產黨"  # 數據屬性
#     # self代表實例本身
#     def __init__(self, names, ages, genders):  # 調用實例化會自動執行__init__
#         # 自動把name,age,gender封裝到self裡並return
#         self.name = names  # 數據屬性
#         self.age = ages
#         self.gender = genders
#     def walk():
#         print("走路")
#     def sleep(self):
#         print("%s睡覺" % self.name)
#     def eat(self, food):
#         print("%s吃%s" % (self.name, food))
#
# p1 = Chinese("jamie", 20, "man")
# # p1.walk()  # => error，因為class會把實例本身(p1)當作參數傳入方法，而walk()沒有參數，所以報錯
# p1.sleep()  # => jamie睡覺，實例調用方法會自動把本身(p1)當參數傳到sleep()
# p1.eat("食物")  # => jamie吃食物


# 作用域
# government = "無黨"
# class Chinese:
#     government = "共產黨"
#     def __init__(self, name):
#         self.name = name
#         print("init-----> %s" % government)
#         # => init-----> 無黨，因他不是用(.)來訪問，因此跟類無關，所以在init中找不到值的話，會直接跳過class到外面找
#
# # 使用點(.)來訪問屬性都會跟類有關，所以訪問時只能在class裡面找
# print("類-----> %s" % Chinese.government)  # => 類-----> 共產黨
# p1 = Chinese("SB")
# print("實例-----> %s" % p1.government)  # => 實例-----> 共產黨

