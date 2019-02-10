# import socket
#
# # AF_INET基於網路協議、SOCK_STREAM基於TCP協議
# phone = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# phone.bind(('127.0.0.1', 8000))  # 綁定ip+port
# phone.listen(5)  # backlog(半連結池)，最多掛起5個連結
#
# print('等客戶端發送消息..')
# conn, addr = phone.accept()  # 等待連結，三次交握成功後拿到 (連結, 地址)
#
# # 信息均為字節類型
# msg = conn.recv(1024)  # 接收消息，信息大小為1024
# print('客戶端發來的信息: ', msg)
# conn.send(msg.upper())  # 發消息
#
# conn.close()  # 斷開連結
# phone.close()


# from socket import *
#
# ip_port = ('127.0.0.1', 8000)
# back_log = 5
# buffer_size = 1024
#
# tcp_server = socket(AF_INET, SOCK_STREAM)
# tcp_server.bind(ip_port)
# tcp_server.listen(back_log)
#
# print('等待接收消息')
# conn, addr = tcp_server.accept()
# print('雙向連結為 ', conn)
# print('客戶端地址為 ', addr)
#
# # data = conn.recv(buffer_size)
# # print('客戶端發來的信息 ', data.decode('utf-8'))
# # conn.send(data.upper())
# while True:
#     data = conn.recv(buffer_size)
#     print('客戶端發來的信息 ', data.decode('utf-8'))
#     conn.send(data.upper())
#
# conn.close()
# tcp_server.close()



from socket import *

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)  # 創建socket服務器
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)  # 這行會重啟ip和端口，這樣就不會造成地址被占用的錯誤
tcp_server.bind(ip_port)  # 將地址綁到服務器
tcp_server.listen(back_log)  # 監聽鏈結

while True:  # 服務器循環(為了讓客戶端段開連結後還能繼續接收其他連結)
    conn, addr = tcp_server.accept()  # 接收客戶端鏈結，並得到 (連結, 地址)
    print('雙向連結為 ', conn)
    print('客戶端地址為 ', addr)

    while True:  # 通訊循環
        try:
            data = conn.recv(buffer_size)
            print('客戶端發來的信息 ', data.decode('utf-8'))
            conn.send(data.upper())
        except Exception:  # 當客戶端段開連結後會報錯，所以直接break掉，進入下一個等待連結的循環
            break

conn.close()
tcp_server.close()