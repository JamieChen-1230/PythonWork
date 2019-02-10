# 雖然進程空間內存是相互獨立的，但還是會有共用資源(ex:屏幕)
from multiprocessing import Process, Lock
import time

# 不加鎖的話有可能會導致同時打印而出錯
def f(lock, i):
    time.sleep(1)
    with lock:    # 等同於lock.acquire() + lock.release()
        print('hello world %s at %s' % (i, time.ctime()))

if __name__ == '__main__':
    lock = Lock()

    for num in range(10):
        Process(target=f, args=(lock, num)).start()
