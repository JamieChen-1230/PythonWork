# tcp的協議數據不會丟，沒有收完包，下次接收，會繼續上次繼續接收，
# 己端總是在收到ack時才會清除緩衝區內容。數據是可靠的，但是會粘包。
from socket import *

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 100

tcp_client = socket(AF_INET, SOCK_STREAM)  # 創建socket客戶端
tcp_client.connect(ip_port)  # 嘗試連結服務器

while True:  # 通訊循環
    msg = input('>>> ').strip()
    if not msg: continue
    if msg == 'break': break
    tcp_client.send(msg.encode('utf-8'))

    data = tcp_client.recv(buffer_size)
    print('服務端發來的信息 ', data.decode('BIG5'))  # 用BIG5是因為我的電腦默認編碼為BIG5

tcp_client.close()