# 整體註釋 ctrl + ?
# -------算數運算(值)-------
num = 9 // 2   # 商
num2 = 9 % 2   # 餘
num3 = 9 ** 2  # 平方

# -------賦值運算(值)-------
# a = a + 1 => a += 1
# a = a // 1 => a //= 1
# ...

# -------比較運算(布林)-------
# 1 != 2

# -------成員運算(布林)-------
# "陳俊宇" 字符串
# "陳" 字符
# "俊宇" 子字符串
name = "陳俊宇"
# if "陳俊" in name:
#     print("OK")
# if "與" not in name:
#     print("OK")
x = "宇" in name  # 布林值
y = not("宇" in name)  # not => 取反值(true false 互換)

# -------邏輯運算(布林)-------
# 沒括號從左到右看
# True遇到and會繼續往下做，若是False遇到and就會直接判斷為False
# False遇到or會繼續往下做，若是True遇到or就會直接判斷為True
z = True and True or False and False
# print(z)  # => True

