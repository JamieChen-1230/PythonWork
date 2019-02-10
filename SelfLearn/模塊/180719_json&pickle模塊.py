# ---------json模塊---------
# json不能處理class數據類型，但任何程式語言都能支持json
import json
# json.dumps() 轉換成json格式
# dic = {'name': "jamie", 'age': 18}
# data = json.dumps(dic)  # 序列化：把對象從內存中變成可存儲或可傳輸的過程
# # {'name': "jamie", 'age': 18} ---> {"age": 18, "name": "jamie"} ---> '{"age": 18, "name": "jamie"}'
# print(data, type(data))  # => {"age": 18, "name": "jamie"} <class 'str'>，為json字符串(內部元素引號都要為雙引號)
# # 66 ---> '66'
# print(json.dumps(66), type(json.dumps(66)))  # => 66 <class 'str'>
# # 's' ---> "s" ---> '"s"'
# print(json.dumps('s'), type(json.dumps('s')))  # => "s" <class 'str'>
# # [1, 2, 3] ---> '[1, 2, 3]'
# print(json.dumps([1, 2, 3]), type(json.dumps([1, 2, 3])))  # => [1, 2, 3] <class 'str'>

# json文件處理，json.loads() 將json字符串轉換為其他數據類型
# dic = {'name': "jamie", 'age': 18}
# data = json.dumps(dic)  # json數據格式
# with open("test_json", "w") as f:
#     f.write(data)
# with open("test_json", "r") as f:
#     j = json.loads(f.read())  # => f.read()出來的是str，反序列化
#     print(j, type(j))  # => {'name': 'jamie', 'age': 18} <class 'dict'>，類型為字典
#     print(j["name"])  # => jamie


# ---------pickle模塊---------
# pickle能處理所有數據類型，但只限於python
import pickle
# dic = {'name': "jamie", 'age': 18}
# data = pickle.dumps(dic)
# print(data, type(data))
# # => b'\x80\x03}q\x00(X\x04\x00\x00\x00nameq\x01X\x05\x00\x00\x00jamieq\x02X\x03\x00\x00\x00ageq\x03K\x12u.' <class 'bytes'>
#
# with open("test_pickle.txt", "wb") as f:  # 要使用wb，因為是字節類型
#     f.write(data)
# with open("test_pickle.txt", "rb") as f:
#     p = pickle.loads(f.read())
#     print(p ,type(p))  # => {'name': 'jamie', 'age': 18} <class 'dict'>


# ---------shelve模塊---------(少用)
# 使用簡易，但也不能跨語言
# import shelve
# with shelve.open("test_shelve") as f:  # 目的：把字典放入文本
#     f["info1"] = {"name": "sb", "age": 87}
#     f["info2"] = {"name": "jamie", "age": 18}
# with shelve.open("test_shelve") as f:
#     print(f.get("info1")["age"])  # => 87
#     print(f.get("info1")["name"])  # => sb

