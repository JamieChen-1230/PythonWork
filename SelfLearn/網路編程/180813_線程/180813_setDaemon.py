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

t_list = []
t1 = threading.Thread(target=music)
t2 = threading.Thread(target=game)
t_list.append(t1)
t_list.append(t2)

if __name__ == '__main__':
    t1.setDaemon(True)  # 設了也沒用，因為主線程會等其他所有線程結束才結束(t2的延遲大於t1)
    for t in t_list:
        # t.setDaemon(True)  # 守護線程，(需要設在start之前)設這個之後會在主線程結束時，強制結束該子線程
        t.start()

    print('finish at %s' % time.ctime())
