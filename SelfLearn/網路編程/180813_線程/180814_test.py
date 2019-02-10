def add():
    sum = 1
    for i in range(10**5):
        sum += i
    print(sum)

def mul():
    sum2 = 1
    for i in range(1, 10**5):
        sum2 *= i
    print(sum2)

import threading ,time
start = time.time()
t1 = threading.Thread(target=add)
t2 = threading.Thread(target=mul)

li = []
li.append(t1)
li.append(t2)

if __name__ == '__main__':
    for t in li:
        t.start()
    # t1.join()
    t2.join()
    print('cost %s' % (time.time()-start))
