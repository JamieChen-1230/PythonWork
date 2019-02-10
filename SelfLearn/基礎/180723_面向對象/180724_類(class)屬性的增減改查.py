# class Chinese:  # 類可以沒有括號，通常首字大寫
#     '這是一個中國人的類'
#     government = "共產黨"  # 數據屬性
#     # self代表實例本身
#     def __init__(self, names, ages, genders):  # 調用實例化會自動執行__init__
#         # 自動把name,age,gender封裝到self裡並return
#         self.name = names  # 數據屬性
#         self.age = ages
#         self.gender = genders
#     def walk(self):
#         print("%s 走路" % self.name)
#     def sleep(self):
#         print("%s 睡覺" % self.name)
#
# # 查詢
# print(Chinese.government)  # => 共產黨
#
# # 修改
# Chinese.government = "民進黨"
# print(Chinese.government)  # => 民進黨
# p1 = Chinese("jamie", 20, "man")
# print(p1.government)  # => 民進黨，修改過後實例的值也會改變
#
# # 增加
# Chinese.country = "中國"
# print(Chinese.country)  # => 中國
# print(p1.country)  # => 中國
#
# # 刪除
# del Chinese.country
# print(Chinese.__dict__)
#
# # 增加、修改函數屬性
# def eat(self, food):
#     print("%s吃%s" % (self.name, food))
# Chinese.eat = eat
# print(Chinese.__dict__)
# p1.eat("水果")
