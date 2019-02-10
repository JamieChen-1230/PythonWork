# I/O多路複用優勢：可以同時監聽多個連結

import socket

sk = socket.socket()
sk.connect(("127.0.0.1", 9904))

while 1:
    inp = input(">>").strip()
    sk.send(inp.encode("utf8"))
    data = sk.recv(1024)
    print(data.decode('utf8'))
