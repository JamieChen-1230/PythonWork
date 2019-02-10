# 當類之間顯著不同且較小的類是較大的類所需的組件時，用組合比較好
# 組合關係寫死
# class School:
#     def __init__(self, name, addr):
#         self.name = name
#         self.addr = addr
#
#     def enroll(self):
#         print("%s 正在招生" % self.name)
#
# class Course:
#     def __init__(self, name, price, period, school):
#         self.name = name
#         self.price = price
#         self.period = period
#         self.school = school
#
# s1 = School("oldboy", "北京")
# s2 = School("oldboy", "南京")
# s3 = School("oldboy", "東京")
#
# c1 = Course("linux", 10, "1hr", s1)
# print(c1.__dict__)
# # => {'price': 10, 'name': 'linux', 'period': '1hr', 'school': <__main__.School object at 0x0000029E37298AC8>}
# print(c1.school.name)  # => oldboy


# 用自定義選單建立組合關聯
# class School:
#     def __init__(self, name, addr):
#         self.name = name
#         self.addr = addr
#
#     def enroll(self):
#         print("%s 正在招生" % self.name)
#
# class Course:
#     def __init__(self, name, price, period, school):
#         self.name = name
#         self.price = price
#         self.period = period
#         self.school = school
#
# s1 = School("oldboy", "北京")
# s2 = School("oldboy", "南京")
# s3 = School("oldboy", "東京")
#
# msg = '''
# 1 北京校區
# 2 南京校區
# 3 東京校區
# '''
# while True:
#     print(msg)
#     menu={
#         "1": s1,
#         "2": s2,
#         "3": s3
#     }
#     choice = input("選擇學校: ")
#     school_addr = menu[choice]
#     name = input("課程名: ")
#     price = input("課程費用: ")
#     period = input("課程時間: ")
#
#     new_course = Course(name, price, period, school_addr)
#     print("課程【%s】屬於%s校區" % (new_course.name, new_course.school.addr))


# 把資訊存起來
# import pickle, time
# class Base:
#     def save(self):
#         with open(self.id, "wb") as f:
#             pickle.dump(self, f)
#
# class School(Base):
#     def __init__(self, name, addr):
#         self.id = str(time.time())
#         self.name = name
#         self.addr = addr
#
# class Course(Base):
#     def __init__(self, name, price, period, school):
#         self.id = str(time.time())
#         self.name = name
#         self.price = price
#         self.period = period
#         self.school = school
#
# s1 = School("台科", "台北")
# s1.save()
# # print(pickle.load(open('1532588954.343552', "rb")).name)




