# ----------------------------------------------
# # name = "小黃"
# # gender = "公"
# # dog_type = "土狗"
# # 狗的特徵
# dog1 = {
#     "name": "小黃",
#     "gender": "公",
#     "dog_type": "土狗"
# }
# dog2 = {
#     "name": "土豆",
#     "gender": "公",
#     "dog_type": "台灣犬"
# }
# person1 = {
#     "name": "jamie",
#     "gender": "男",
#     "dog_type": "人"
# }
#
# # 狗的行為
# def bark(dog):
#     print("%s 汪汪汪~" % dog["name"])
# def run(dog):
#     print("%s 跑啊跑~" % dog["name"])
#
# bark(dog1)
# bark(person1)  # 為什麼人也能做狗的行為(X)

# ----------------------------------------------
# def dog():
#     # 狗的行為
#     def bark(dog):
#         print("%s 汪汪汪~" % dog["name"])
#     def run(dog):
#         print("%s 跑啊跑~" % dog["name"])
#
#     dog1 = {
#         "name": "小黃",
#         "gender": "公",
#         "dog_type": "土狗",
#         "bark": bark,
#         "run": run
#     }
#     return dog1
#
# dog1 = dog()
# print(dog1)
# dog1["bark"](dog1)

# # ----------------------------------------------
# def dog(name, gender, type):
#     # 狗的行為
#     def bark(dog):
#         print("%s 汪汪汪~" % dog["name"])
#     def run(dog):
#         print("%s 跑啊跑~" % dog["name"])
#
#     d = {
#         "name": name,
#         "gender": gender,
#         "dog_type": type,
#         "bark": bark,
#         "run": run
#     }
#     return d
#
# dog1 = dog("小黃", "公", "土狗")
# dog2 = dog("土豆", "公", "土狗")
# dog1["bark"](dog1)
# dog2["run"](dog2)

# ----------------------------------------------面向對象設計(特徵與動作結合)
# def dog(name, gender, type):
#     # 狗的行為
#     def bark(dog):
#         print("%s 汪汪汪~" % dog["name"])
#     def run(dog):
#         print("%s 跑啊跑~" % dog["name"])
#     # 初始化
#     def init(name, gender, type):
#         dog_data = {
#             "name": name,
#             "gender": gender,
#             "dog_type": type,
#             "bark": bark,
#             "run": run
#         }
#         return dog_data
#     return init(name, gender, type)
#
# dog1 = dog("小黃", "公", "土狗")
# dog2 = dog("土豆", "公", "土狗")
# dog1["bark"](dog1)
# dog2["run"](dog2)
