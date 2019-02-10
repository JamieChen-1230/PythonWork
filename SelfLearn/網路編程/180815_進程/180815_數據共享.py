# 可共享數據類型：
# list,  dict,  Namespace,  Lock,  RLock,  Semaphore,  BoundedSemaphore,
# Condition,  Event,  Barrier,  Queue,  Value and  Array

from multiprocessing import Process, Manager


def f(d, l, n):
    d[n] = '1'    # {n: '1'}
    d['name'] = 'sb'  # {0: '1', '2': 2, 0.25: None}
    l.append(n)  # [0,1,2,3,4,n]

if __name__=='__main__':

    with Manager() as manager:
        d = manager.dict()  # 創建可共享字典
        l = manager.list("SB")  # 創建可共享列表 ['S', 'B']

        p_list = []
        for i in range(10):
            p = Process(target=f, args=(d, l, i))
            p.start()
            p_list.append(p)

        for res in p_list:
            res.join()

        print('共享字典', d)
        print('共享列表', l)
