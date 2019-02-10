import threading
import time

def music():
    print('start to listen at %s' % time.ctime())
    time.sleep(2)  # sleep等同於I/O操作
    print('end to listen at %s' % time.ctime())

def game():
    print('start to play at %s' % time.ctime())
    time.sleep(4)
    print('end to play at %s' % time.ctime())


if __name__ == '__main__':
    t1 = threading.Thread(target=music)
    t2 = threading.Thread(target=game)
    t3 = threading.Thread(target=music)
    t1.start()
    t2.start()

    t1.join()  # t1子線程結束前，之後的主線程不會被執行
    # t2.join()
    t3.start()
    print('end')
