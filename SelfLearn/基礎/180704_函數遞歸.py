# 錯誤示範
# def calc(n):
#     print(n)
#     calc(n)
# calc(10)  # => 報錯 因超過遞歸循環上限(死循環)

# 必須有明確的結束條件
# def calc(n):
#     print(n, end=" ")
#     if int(n/2) == 0:
#         return n  # 遇到return就會結束函數
#     return calc(int(n/2))
# calc(10)  # => 10 5 2 1

# 問路問題
# def ask_way(person_list):
#     print("-"*60)
#     if len(person_list) == 0:
#         return "沒人知道"
#     person = person_list.pop(0)
#     print("hi, %s!! 你知道這在哪嗎?" % person)
#     if person == "596":
#         return "%s說：我知道" % person
#     print("%s說：我不知道ㄟ，我幫你問問%s" % (person,person_list))
#
#     return ask_way(person_list)
# res = ask_way(['sb', '87', 'jamie', '596'])
# print(res)

