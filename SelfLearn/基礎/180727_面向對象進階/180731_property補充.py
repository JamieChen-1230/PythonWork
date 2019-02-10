# class Foo:
#     @property
#     def AAA(self):
#         print('get的時候運行我')
#
#     @AAA.setter  # 在使用靜態屬性的時候無法設定值，所以需額外定義
#     def AAA(self, val):
#         print('set的時候運行我', val)
#
#     @AAA.deleter  # 在使用靜態屬性的時候無法刪除值，所以需額外定義
#     def AAA(self):
#         print('delete的時候運行我')
#
# f1 = Foo()
# f1.AAA
# f1.AAA = 1
# del f1.AAA

# 功能同上
# class Foo:
#     def get_AAA(self):
#         print('get的時候運行我')
#
#     def set_AAA(self, val):
#         print('set的時候運行我', val)
#
#     def del_AAA(self):
#         print('delete的時候運行我')
#
#     AAA = property(get_AAA, set_AAA, del_AAA)
#
# f1 = Foo()
# f1.AAA
# f1.AAA = 1
# del f1.AAA


# 應用
# class Item:
#     def __init__(self):
#         self.start_price = 100
#         self.discount = 0.8
#
#     @property
#     def price(self):
#         value = self.start_price * self.discount
#         return value
#
#     @price.setter
#     def price(self, val):
#         self.start_price = val
#
#     @price.deleter
#     def price(self):
#         del self.start_price
#
# i1 = Item()
# print(i1.price)  # => 80.0
# i1.price = 200
# print(i1.price)  # => 160.0
# del i1.price
# # print(i1.price)  # => error，因為start_price屬性已被刪除
