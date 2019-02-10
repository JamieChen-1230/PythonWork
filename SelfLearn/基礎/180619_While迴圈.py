# python2使用中文需加-*- coding:utf8 -*-，python3則不用宣告
# 變量，只能由字母、數字、下底線組成，且不能以數字開頭

# count = 0
# while count < 10:
#     if count == 5 or count == 6:
#         count = count + 1
#         continue  # 終止當前循環，直接跳下一循環
#     print(count)
#     if count == 8:
#         break  # 跳出所有循環，連else也不會執行
#     count = count + 1
# else:
#     print("out")

count = 1
while count <= 3:
    # input取得用戶輸入值
    password = input("請輸入： ")  # input出來都是字串
    if password == "123":
        print("登入成功")
        break
        # print(type(password))
    else:
        print("登入失敗，你還有" + str(3-count) + "次輸入機會")
    count = count + 1
else:
    print("請稍後再嘗試登入")
