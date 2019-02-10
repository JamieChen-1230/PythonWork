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
# p1 = Chinese("jamie", 20, "man")
#
# # 查詢
# print(p1.gender)  # => man
#
# # 修改、增加
# print(p1.government)  # => 共產黨
# p1.government = "無黨"  # 修改的只是修改p1實例的值
# print(p1.government)  # => 無黨
# print(Chinese.government)  # => 共產黨
# print(p1.__dict__)  # => {'government': '無黨', 'age': 20, 'name': 'jamie', 'gender': 'man'}
# p2 = Chinese("jamie2", 20, "man")
# print(p2.__dict__)  # => {'age': 20, 'name': 'jamie2', 'gender': 'man'}，p1修改不影響p2
#
# # 刪除
# del p1.government
# print(p1.__dict__)  # => {'name': 'jamie', 'age': 20, 'gender': 'man'}
