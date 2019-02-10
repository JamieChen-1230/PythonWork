# 如果函數內無global關鍵字
#       -有聲明局部變量：讀取局部變量，且無法對全局變量重新賦值
#       -無聲明局部變量：讀取全局變量，且無法對全局變量重新賦值，但可以進行內部元素操作
# 如果函數內有global關鍵字
#       -有聲明局部變量：此局部變量被當作全局變量操作
#       -無聲明局部變量：讀取全局變量，且可以對全局變量重新賦值，也可以進行內部元素操作
# 全局變量用大寫，局部變量小寫，方便以後程式瀏覽

# name = "Jamie"  # 全局變量(未縮進)
# def subroutine_1():
#     x = 1  # 局部變量(有縮進)
#     print(name)  # => Jamie，子程序也能調用全局變量
#     return x
# print(subroutine_1())  # => 1

# name = "Jamie"  # 全局變量
# def subroutine_2():
#     name = "SB"  # 局部變量，跟外面的全局變量毫無關係
#     print(name)  # => SB 若全局變數和局部變數名稱相同時，優先使用"局部變量"
# print(subroutine_2())  # => None
# print(name)  # => Jamie 局部變量不會影響全局變量

# name = "Jamie"  # 全局變量
# def subroutine_3():
#     global name  # 把name設為全局變量
#     name = "SB"  # 全局變量，並重新賦值給全局變量
#     print(name)  # => SB
# subroutine_3()
# print(name)  # => SB 因在子程序內已被改變

# name = ["Jamie", "sb"]  # 全局變量
# def subroutine_4():
#     name.append("nb")  # 可以進行內部元素操作
#     print(name)  # => ['Jamie', 'sb', 'nb']
# subroutine_4()
# print(name)  # => ['Jamie', 'sb', 'nb']

# def a():
#     name = "a"
#     print(name, end=" ")  # a
#     def b():
#         name = "b"
#         print(name, end=" ")  # b
#         def c():
#             name = "c"
#             print(name, end=" ")  # c
#         print(name, end=" ")  # b
#         c()
#     b()
#     print(name, end=" ")  # a
# a()  # => a b b c a

# name = "jamie"
# def a():
#     name = "sb"
#     def b():
#         global name  # 全局變量(name = "jamie")
#         name = "87"
#     b()
#     print(name)  # => sb，因優先讀取局部變量
# print(name)  # => jamie
# a()
# print(name)  # => 87 因在b()中更改了全局變量

# name = "jamie"
# def a():
#     name = "sb"
#     def b():
#         nonlocal name  # 上一級變量(name = "sb")
#         name = "87"
#     b()
#     print(name)  # => 87 因在b()中更改了上一級變量
# print(name)  # => jamie
# a()
# print(name)  # => jamie 沒global去改動

# name = "jamie"
# def a(func):
#     name = "sb"
#     func()
# def b():
#     print(name)  # => jamie，func()只是指向b()的函數體，不代表是在a()中運行
# a(b)
