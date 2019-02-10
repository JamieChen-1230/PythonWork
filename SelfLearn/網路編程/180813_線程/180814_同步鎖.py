import time
import threading
num = 100

def sub():
    global num
    # num -= 1
    lock.acquire()  # 在執行lock的區間內不允許cpu切換
    temp = num
    time.sleep(0.001)  # 因為停了0.001秒導致有些線程在抓取num賦值給temp時會抓到同一個值
    num = temp-1
    lock.release()

li = []
lock = threading.Lock()  # 同步鎖
for t in range(100):
    t = threading.Thread(target=sub)
    t.start()
    li.append(t)
    print(threading.active_count())

for i in li:
    i.join()

print('num', num)
