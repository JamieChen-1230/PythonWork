# import socket
# import select
#
# sk = socket.socket()
# sk.bind(("127.0.0.1", 9904))
# sk.listen(5)
#
# while True:
#     # select監聽server_sk
#     # 水平觸發 EX：有人發出請求(高電平1)
#     r, w, e = select.select([sk, ], [], [], 3)  # 參數：input, output, errput, 一次監聽幾秒(默認為一直監聽)
#     print(r)
#     for i in r:  # r = [sk,]
#         # EX：把請求接收到用戶態(低電平0)
#         conn, addr = i.accept()  # conn, addr 為 client_sk
#         print(conn)
#         print("hello")
#     # print(r)
#     print('>>>>>>')


# ---I/O多路複用優勢：可以同時監聽多個連結---
# import socket
# import select
#
# sk = socket.socket()
# sk.bind(("127.0.0.1", 9904))
# sk.listen(5)
# inp = [sk, ]
# while True:
#
#     # select監聽server_sk
#     r, w, e = select.select(inp, [], [], 3)  # 參數：input, output, errput, 一次監聽幾秒(默認為一直監聽)
#     print(r)
#     for i in r:  # r = [sk,]
#         conn, addr = i.accept()  # conn, addr 為 client_sk
#         print(conn)
#         print("hello")
#         inp.append(conn)
#     print('>>>>>>')


# 透過多路複用實現併發
import socket
import select
sk = socket.socket()
sk.bind(("127.0.0.1", 9904))
sk.listen(5)
inputs = [sk, ]

while True:
    r, w, e = select.select(inputs, [], [], 5)

    for obj in r:
        if obj == sk:  # 判斷是否是新連結進來
            conn, add = obj.accept()
            print(conn)
            inputs.append(conn)
        else:  # 還是conn要send, recv
            data_byte = obj.recv(1024)
            print(str(data_byte, 'utf8'))
            inp = input('回答%s號客戶>>> ' % inputs.index(obj))
            obj.sendall(bytes(inp, 'utf8'))

    print('>>', r)
