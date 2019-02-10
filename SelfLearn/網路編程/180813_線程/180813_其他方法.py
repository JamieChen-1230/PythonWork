import threading
import time

def music():
    print('start to listen at %s' % time.ctime())
    time.sleep(2)
    print('end to listen at %s' % time.ctime())

def game():
    print('start to play at %s' % time.ctime())
    time.sleep(4)
    print('end to play at %s' % time.ctime())


if __name__ == '__main__':
    t1 = threading.Thread(target=music)
    t1.setName('music~')  # 設名稱
    t2 = threading.Thread(target=game)
    t1.start()  # 啟動線程
    t2.start()
    print(t1.isAlive())  # => True，判斷線程是否還在運行中
    print(t1.getName())  # => music~，查看名稱
    print(threading.active_count())  # => 3，目前有幾個線程在執行(包括主線程)


# -----------------調用方式二-----------------
# print('-----------------調用方式二-----------------')
# class MyThread(threading.Thread):
#     def __init__(self, num):
#         threading.Thread.__init__(self)
#         self.num = num
#
#     def run(self):  # 定義每個線程要運行的程序
#         print('running %s at %s' % (self.num, time.ctime()))
#         time.sleep(3)
#         print('end %s at %s' % (self.num, time.ctime()))
#
# if __name__ == '__main__':
#     t1 = MyThread(1)
#     t2 = MyThread(2)
#     t1.start()
#     t2.start()
