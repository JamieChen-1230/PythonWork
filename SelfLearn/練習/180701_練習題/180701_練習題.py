# 相加"5+9"
# value = "5+9"
# v1, v2 = value.split("+")
# print(int(v1)+int(v2))

# 計算使用者輸入的字母數和數字數
# content = input(">>>")
# a=0
# b=0
# for i in content:
#     if i.isdigit():
#         a += 1
#     if i.isalpha():
#         b += 1
# print("數字個數：", a)
# print("字母個數：", b)

# 把使用者輸入的資料排版並輸出
# result = ""
# while 1:
#     name = input("name>>>")
#     age = input("age>>>")
#     email = input("email>>>")
#     template = "{0}\t{1}\t{2}\n"
#     v = template.format(name, age, email)
#     v = v.expandtabs(10)
#     result = result + v
#     a = input("是否繼續輸入(y/n)")
#     if a == "n":
#         break
# print(result)

# 1,2,3,4,5,6,7,8 組成十位和個位不相同的所有值
# for i in range(1, 9):
#     for j in range(1,9):
#         if i != j:
#             print(str(i)+str(j))

# 99乘法
# for i in range(1, 10):
#     for j in range(1, 10):
#         print(str(j) + " * " + str(i) + " = " + str(i*j) + "\t", end="")  # end參數默認為"\n"
#     print("")

# 公雞5元，母雞3元，小雞1/3元，我要買100隻，如何買剛剛好100元(三種雞都要)
# count = 0
# for x in range(1, 100//5):  # x最多買100//5隻
#     for y in range(1, 100//3):
#         count += 1
#         if ((5 * x + 3 * y + 1/3 * (100-x-y)) == 100) and (100-x-y) != 0:
#             print(x, y, (100-x-y))
# print(count)

# 列表元素以"_"串接
# li = [123, "fff", 55, "d"]
# s = ""
# for i in li:
#     if i != li[-1]:
#         s += str(i) + "_"
#     else:
#         s += str(i)
# print(s)

# 打印元組元素和索引
# tu =("一", "二", "三", "四")
# for a, b in enumerate(tu, 10):  # 10 => 表示序號從10開始
#     print(a, b)

# 人口普查
# def get_populaation():
#     with open("人口.txt", 'r', encoding='utf-8') as f:
#         for i in f:
#             yield i   # 回傳的是字符串形式
# res = get_populaation()
#
# # all_pop = 0  # 不好的方法
# # for i in res:
# #     # eval()先把字符串中的字典格式提取出來
# #     res_dic = eval(i)
# #     all_pop+=res_dic['population']
#
# all_pop = sum(eval(i)['population'] for i in res)  # 好的方法
# print(all_pop)  # => 3453460340

# 用函數遞歸算5!
# def f(n):
#     if n == 1:
#         return 1
#     return n*f(n-1)
# res = f(5)
# print(res)  # => 120

# 跳出所有while循環
# tag = True
# while tag:
#     print("1")
#     i = input("1>> ").strip()
#     if i == "quit": break
#     if i == "quit_all": tag = False
#     while tag:
#         print("2")
#         i = input("2>> ").strip()
#         if i == "quit": break
#         if i == "quit_all": tag = False
#         while tag:
#             print("3")
#             i = input("3>> ").strip()
#             if i == "quit": break
#             if i == "quit_all": tag = False

# 用正則表達式計算 "12+(34*6+2-5*(2-1))"
# print(eval("12+(34*6+2-5*(2-1))"))  # => 213

# import re
# num = "12+(34*6+2-5*(2-1))"
# print(re.findall("\([^()]*\)", num))  # => ['(2-1)']
