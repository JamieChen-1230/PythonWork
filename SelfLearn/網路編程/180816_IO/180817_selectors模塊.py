import selectors
import socket

sel = selectors.DefaultSelector()

def accept(sock, mask):
    conn, addr = sock.accept()   # Should be ready
    print('accepted', conn, 'from', addr)
    conn.setblocking(False)
    sel.register(conn, selectors.EVENT_READ, read)

def read(conn, mask):
    data = conn.recv(1000)   # Should be ready
    if data:
        print('echoing', repr(data), 'to', conn)
        conn.send(data)   # Hope it won't block
    else:
        print('closing', conn)
        sel.unregister(conn)
        conn.close()

sock = socket.socket()
sock.bind(('localhost', 1234))
sock.listen(100)
sock.setblocking(False)

sel.register(sock, selectors.EVENT_READ, accept)  # 註冊(將sock和accept做綁定)

while True:
    events = sel.select()  # 監聽
    print(events)
    for key, mask in events:
        print(key, mask)
        callback = key.data
        callback(key.fileobj, mask)
