# -----第一層意義：類就是麻袋，本身就是一種封裝-----
# class Chinese:  # 類可以沒有括號，通常首字大寫
#     '這是一個中國人的類'
#     government = "共產黨"  # 數據屬性
#     # self代表實例本身
#     def __init__(self, names, ages, genders):  # 調用實例化會自動執行__init__
#         # 自動把name,age,gender封裝到self裡並return
#         self.name = names  # 數據屬性
#         self.age = ages
#         self.gender = genders
#
#     def sleep(self):
#         print("%s睡覺" % self.name)
#
# print(Chinese.__dict__)
# # Chinese裡面裝了各種不同屬性(裝)，且外部調用者無法得知方法內的實際內容(封)


# -----第二層意義：類中定義私有的，表只能在類內部使用，外部無法訪問----- (這層只是種約定)
# _變數
# class Chinese:
#     '這是一個中國人的類'
#     _government = "共產黨"  # 單下滑線開頭表示對外隱藏
#     # self代表實例本身
#     def __init__(self, names, ages, genders):
#         self.name = names
#         self.age = ages
#         self.gender = genders
#
#     def sleep(self):
#         print("%s睡覺" % self.name)
#
# p1 = Chinese("jamie", 20, "man")
# print(p1._government)  # => 共產黨，還是可以被調用，因為這只是種約定，為了讓大家知道這個不應該被調用

# __變數
# class Chinese:
#     '這是一個中國人的類'
#     __government = "共產黨"  # 雙下滑線開頭也表示對外隱藏，且會對變量重新命名
#     # self代表實例本身
#     def __init__(self, names, ages, genders):
#         self.name = names
#         self.age = ages
#         self.gender = genders
#
#     def sleep(self):
#         print("%s睡覺" % self.name)
#
#     def info(self):
#         print(self.__government)  # 內部能直接訪問
#
# p1 = Chinese("jamie", 20, "man")
# # print(p1.__government)  # => error
# print(p1._Chinese__government)  # => 共產黨，已被重新命名，但還是可被調用，所以也只是一種約定
# p1.info()  # => 共產黨

