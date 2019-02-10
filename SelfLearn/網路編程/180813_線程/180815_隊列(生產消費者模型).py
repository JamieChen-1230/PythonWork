import time, random
import queue, threading

q = queue.Queue()

def Producer(name):
    count = 0
    while count < 10:
        print("making........")
        time.sleep(5)  # 隨機睡1~2s
        q.put(count)
        print('Producer %s has produced %s baozi..' % (name, count))
        count += 1
        # q.task_done()  # 告訴隊列成功放進了一個包子
        q.join()
        print("ok......")

def Consumer(name):
    count = 0
    while count < 10:
        time.sleep(random.randrange(2, 4))
        # print('waiting.......')
        # q.join()  # 在沒有收到q.task_done()信號前，會在這等待
        data = q.get()
        print('eating........')
        time.sleep(4)
        q.task_done()
        print('\033[32;1mConsumer %s has eat %s baozi...\033[0m' % (name, data))
        count += 1

p1 = threading.Thread(target=Producer, args=('A廚師',))
c1 = threading.Thread(target=Consumer, args=('B顧客',))
c2 = threading.Thread(target=Consumer, args=('C顧客',))
c3 = threading.Thread(target=Consumer, args=('D顧客',))
p1.start()
c1.start()
c2.start()
c3.start()
