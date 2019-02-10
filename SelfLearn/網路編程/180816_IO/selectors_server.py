# 異步
import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()   # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)  # 設為非阻塞
    sel.register(conn, selectors.EVENT_READ, read)  # 註冊(將conn和read做綁定)

def read(conn, mask):
    try:
        data = conn.recv(1000)   # Should be ready
        if not data:
            raise Exception
        print('echoing', data, 'to', conn)
        conn.send(data)  # Hope it won't block
    except Exception as e:
        print('closing', conn)
        sel.unregister(conn)  # 解除註冊
        conn.close()


sock = socket.socket()
sock.bind(('localhost', 1234))
sock.listen(100)
sock.setblocking(False)

sel.register(sock, selectors.EVENT_READ, accept)  # 註冊(將sock和accept做綁定)

while True:
    events = sel.select()  # 監聽
    # print(events)
    for key, mask in events:
        # print(key, mask)
        callback = key.data  # sel.register裡第三個參數(accept或read)
        callback(key.fileobj, mask)  # sel.register裡的第一個參數(sock或conn)
