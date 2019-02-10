# 當類之間有很多相同功能，可以用"繼承"來提取這些共同功能為基類

# 一般繼承
# 子類繼承父類的所有屬性
# class Dad:
#     '父類'
#     money = 10
#     def __init__(self,name):
#         print("父")
#         self.name = name
#     def hit_son(self):
#         print("%s 正在打兒子" % self.name)
#
# class Son(Dad):  # 單繼承
#     pass
#
# # print(Son.money)  # => 10
# # print(Dad.__dict__)
# # print(Son.__dict__)  # => {'__module__': '__main__', '__doc__': None}，沒有父類屬性
#
# s1 = Son("jamie")  # 觸發的是父類的__init__
# print(s1.name)  # => jamie
# print(s1.money)  # => 10
# s1.hit_son()  # => jamie 正在打兒子


# 屬性重名：子類先在自身類找，找不到才去找父類的
# class Dad:
#     '父類'
#     money = 10
#     def __init__(self,name):
#         print("父")
#         self.name = name
#     def hit_son(self):
#         print("%s 正在打兒子" % self.name)
#
# class Son(Dad):  # 單繼承
#     '子類'
#     money = 100000
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
#
# s1 = Son("jamie", 18)  # 觸發的是父類的__init__
# print(s1.money)  # => 100000
# print(Dad.money)  # => 10
# s1.hit_son()  # => jamie 正在打兒子


# 街口繼承：定義一個基類，並把裡面的方法定義成街口函數
# 讓欲繼承基類的子類須各自定義與街口函數相同的方法才可實例化
# import abc
# class All_file(metaclass=abc.ABCMeta):
#     @abc.abstractmethod  # 街口函數
#     def read(self):  # 街口類方法不須實現，所以不用定義內容
#         pass
#     @abc.abstractmethod
#     def write(self):
#         pass
#
# class Disk(All_file):
#     def read(self):  # 必須定義，否則無法實例化
#         print("disk read")
#     def write(self):  # 必須定義，否則無法實例化
#         print("disk write")
#
# d1 = Disk()
# d1.read()

