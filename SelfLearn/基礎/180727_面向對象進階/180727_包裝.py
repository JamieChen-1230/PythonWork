# 包裝：二次加工
# 透過繼承新增、修改方法，其他功能則保持原樣

# class List(list):
#     pass
# li = List("jamie")
# print(li, type(li))  # => ['j', 'a', 'm', 'i', 'e'] <class '__main__.List'>
# li2 = list('jamie')
# print(li2, type(li2))  # => ['j', 'a', 'm', 'i', 'e'] <class 'list'>


# 透過包裝訂製自己的數據類型
class List(list):
    def show_mid(self):  # 派生
        mid_index = int(len(self)/2)
        return self[mid_index]

    def append(self, value):
        if type(value) is str:  # 限制只能append字符串
            super().append(value)  # 調用父類(list)的append方法

li = List("jamie")
print(li.show_mid())  # => m
li.append("SB")
print(li)  # => ['j', 'a', 'm', 'i', 'e', 'SB']
