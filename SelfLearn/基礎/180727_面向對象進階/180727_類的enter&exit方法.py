# 上下文管理協議
# class Open:
#     def __init__(self, name):
#         self.name = name
#     def __enter__(self):
#         print("執行enter")
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):  # exit的運行完畢就代表了with運行完畢
#         print('執行exit')
#         print('exc_type', exc_type)
#         print('exc_val', exc_val)
#         print('exc_tb', exc_tb)
#
# # Open('a.txt')  # 觸發enter，並產生對象
# with Open('a.txt') as f:  # enter會return Open產生的對象 給f
#     print(f)  # => <__main__.Open object at 0x000001B7E6A12F60>
#     print(qwert)  # 當發生錯誤異常後會停止運行之後的代碼，直接觸發exit
#     print(f.name)  # => a.txt
#     # 若無發生異常，with裡代碼運行結束後觸發exit
# print("結束")  # 不會打印，因為前面已發生異常


# __exit__ return True
# class Open:
#     def __init__(self, name):
#         self.name = name
#     def __enter__(self):
#         print("執行enter")
#         return self
#     def __exit__(self, exc_type, exc_val, exc_tb):  # exit的運行完畢就代表了with運行完畢
#         print('執行exit')
#         print('exc_type', exc_type)
#         print('exc_val', exc_val)
#         print('exc_tb', exc_tb)
#         return True  # 回傳True的話不會跳出異常警告
#
# # Open('a.txt')  # 觸發enter，並產生對象
# with Open('a.txt') as f:  # enter會回傳【Open產生的對象給f
#     print(f)  # => <__main__.Open object at 0x000001B7E6A12F60>
#     print(qwert)  # 當發生錯誤異常後會停止運行之後的代碼，直接觸發exit
#     print(f.name)  # => a.txt】
#     # 若無發生異常，with裡代碼運行結束後觸發exit
# print("結束")  # 會打印，因為exit已經吃掉了異常，所以會繼續執行
