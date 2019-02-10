# --------隊列通信--------
# # import queue
# import multiprocessing
# import time
#
# def sub(q):
#     print('sub id', id(q))
#     print('sub time', time.ctime())
#     time.sleep(1)
#     q.put(87)
#     q.put("jamie")
#
# def main():
#     print('main id', id(q))
#     print(q.get(), time.ctime())
#     print(q.get(), time.ctime())
#
# if __name__ == '__main__':
#     # q = queue.Queue()
#     q = multiprocessing.Queue()  # 要用進程隊列
#     p = multiprocessing.Process(target=sub, args=(q,))  # q是複製過去的，不是同一個queue
#     p.start()
#     main()


# --------管道--------
# from multiprocessing import Process, Pipe
#
# def f(conn):
#     conn.send([12, {"name": "yuan"}, 'hello'])
#     response = conn.recv()
#     print("response", response)
#     print("child_conn_ID2:", id(conn))
#     conn.close()
#
# if __name__ == '__main__':
#     parent_conn, child_conn = Pipe()  # 雙向管道
#     print("child_conn_ID1:", id(child_conn))
#     p = Process(target=f, args=(child_conn, ))  # 要把conn的一端接口給子進程
#     p.start()
#
#     print(parent_conn.recv())    # prints "[42, None, 'hello']"
#     parent_conn.send("兒子你好!")
#     p.join()
