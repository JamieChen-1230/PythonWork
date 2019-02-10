# 1.定義函數(執行函數是調用變量而不是複製一個新的變量)
# def test(x):  # x為形參，形參不占用內存只有被調用時，才會暫時佔用內存
#     '''
#     函數註釋
#     :param x:整數
#     :return:y:計算結果
#     '''
#     y = 2*x+1
#     return y
#
# 過程：沒有返回值的函數
# def test2():
#     print("hello")
#
# def test3():
#     return 1, "2", ["jamie"], (1, 2)
#
# t1 = test(5)  # 5是實參
# t2 = test2()
# t3 = test3()
#
# print(t1)  # => 11  返回一個值時，返回object
# print(t2)  # => None  返回零個值時，返回None
# print(t3)  # => (1, '2', ['jamie'], (1, 2)) 返回多個值時，返回一個元組

# 2.位置參數(需對應位置順序)、關鍵字參數(無須對應位置)，兩者參數數多一少一都不行
# def test(x, y, z):
#     print(x)
#     print(y)
#     print(z)
#
# test(1, z=3, y=2)  # => 1 2 3  位置參數必須放在關鍵字參數之前

# 3.默認參數
# def test(x, y, z=10):  # 默認參數項須放在最後
#     print(x)
#     print(y)
#     print(z)
# test(1, 2)  # => 1 2 10  z不輸入值的話，則使用默認參數值

# 4.參數組(**字典, *元組、列表)
# def test(x, *args):  # args不輸入參數也可以，輸入多餘的值會被轉成元組存在args(args用來解決多餘的位置參數)
#     print(x)
#     print(args)
# test(1, 2, 3, 4, 5, 6)  # => 1 (2, 3, 4, 5, 6)
# test(1, ["x", "y", "z"])  # => 1 (['x', 'y', 'z'])  沒加*的話，就會被當作是一個整體
# test(1, *["x", "y", "z"])  # => 1 ('x', 'y', 'z')

# def test2(x, **kwargs):  # kwargs用來解決多餘的關鍵字參數
#     print(x)
#     print(kwargs)
#
# test2(1, y1=2, y2=3, y3=4)  # => 1 {'y3': 4, 'y2': 3, 'y1': 2}
# test2(1, **{"y1": 2, "y2": 3, "y3": 4})  # => 1 {'y3': 4, 'y2': 3, 'y1': 2}

# def test3(x, *args, **kwargs):  # args須放在kwargs前
#     print(x)
#     print(args)
#     print(kwargs)
#
# test3(1, 2, 3, 4, 5, x=1, y=2, z=3)  # => 報錯  因為x重複給值
# test3(1, 2, 3, 4, 5, y=2, z=3)  # => 1 (2, 3, 4, 5) {'z': 3, 'y': 2}
# test3(1, *(2, 3, 4, 5), **{'z': 3, 'y': 2})  # => 1 (2, 3, 4, 5) {'z': 3, 'y': 2}

# 5.前項引用
# def b():
#     print("b", end=" ")
# def a():
#     print("a", end=" ")
#     b()
# a()  # => a b

# def a():  # 函數未調用前不會執行
#     print("a", end=" ")
#     b()
# def b():
#     print("b", end=" ")
# a()  # => a b 函數順序沒差，因為都是加載到內存

# def a():
#     print("a", end=" ")
#     b()
# a()  # => 報錯 因為b()還未加載到內存
# def b():
#     print("b", end=" ")


