# -------------------列表-------------------
# import threading, time
# li =[1,2,3,4,5]
#
# def pri(name):
#     while li:
#         a = li[-1]
#         print(name, a)
#         time.sleep(1)
#         try:
#             li.remove(a)
#         except Exception as e:
#              print('----', name, a, e)
#
# t1 = threading.Thread(target=pri, args=('t1',))
# t1.start()
# t2 = threading.Thread(target=pri, args=('t2',))
# t2.start()


# -------------------線程隊列-------------------
# ----------Queue----------
# import queue  # 線程隊列
#
# # queue.LifoQueue(maxsize)
# # queue.PriorityQueue(maxsize)
# # maxsize參數為隊列大小
# q = queue.Queue(maxsize=5)  # 默認是FIFO
#
# q.put(87)  # 加入數據
# q.put('sb')
# q.put({'name': 'nb'})
# # q.put(34, block=False)  # block默認為True，當False時且隊列滿的話則報錯
#
# while 1:
#     # data = q.get(block=False)  # get()也有block參數
#     data = q.get()  # 取數據，沒值時會卡在這
#     print(data)
#     print('---------')

# ----------PriorityQueue----------
# import queue
#
# q = queue.PriorityQueue(maxsize=5)
#
# q.put([3, 87])
# q.put([1, 'sb'])
# q.put([2, {'name': 'nb'}])
#
# while 1:
#     data = q.get()
#     print(data[1])
#     print('---------')

# ----------其他方法----------
# import queue  # 線程隊列
# q = queue.Queue(maxsize=5)
#
# # q.put_nowait() 同等於 q.put(block=False)
# q.put(87)
# q.put('sb')
# q.put({'name': 'nb'})
#
# print(q.qsize())  # 目前隊列長度
# print(q.empty())  # 是否為空
# print(q.full())   # 是否為滿
#
# while 1:
#     print('---------')
#     # q.get_nowait() 同等於 q.get(block=False)
#     data = q.get()
#     print(data)
