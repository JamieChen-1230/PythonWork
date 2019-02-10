# 異常處理：捕捉異常成功則進入另一個處理分支，使程式不會崩潰
# 雖然用if也能處理異常但會有重複代碼與影響程式可讀性的問題
# try...except...盡量少用，用太多也會影響可讀性

# try...except...
# try:
#     被測試代碼(主邏輯)
# except 異常類型:
#     try中檢測到異常後執行的代碼

# 指定異常處理
# try:
#     age = input(">> ")
#     int(age)  # 發生異常後就不會執行之後的代碼，直接跳到except
#     print(age)
# except ValueError as e:
#     print(e)  # 返回異常值

# 不指定異常處理
# try:
#     age = input(">> ")
#     int(age)
#     print(age)
#     li = []
#     li[10]
# except Exception as e:
#     print(e)  # 返回異常值

# 其他的異常處理
# else 沒有異常發生時執行
# try:
#     age = input(">> ")
#     int(age)
# except ValueError as e:
#     print(e)
# else:
#     print('無異常')
# print('End')

# finally 不管是否發生異常都會執行
# try:
#     age = input(">> ")
#     int(age)
# except ValueError as e:
#     print(e)
# finally:
#     print('不管是否發生異常都會執行，通常是用來進行清理操作')
# print('End')

# 主動觸發異常
# raise ValueError("XXXXX")

# 自定義異常(異常為一種類)
# class SbError(BaseException):
#     def __init__(self, msg):
#         self.msg = msg
#
# raise SbError('自定義異常')

# 斷言 assert
# print("==========================")
# assert 1 == 1
#
# print('--------------------------')
#
# def test():
#     return 1
# res = test()
# assert res == 2
