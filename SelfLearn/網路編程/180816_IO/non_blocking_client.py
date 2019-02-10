import time
import socket
sk = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

while True:
    sk.connect(('127.0.0.1', 6667))
    print("hello")
    sk.sendall(bytes("hello", "utf8"))
    time.sleep(2)
    break
