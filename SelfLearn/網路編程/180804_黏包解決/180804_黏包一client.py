# tcp的協議數據不會丟，沒有收完包，下次接收，會繼續上次繼續接收，
# 己端總是在收到ack時才會清除緩衝區內容。數據是可靠的，但是會粘包。
from socket import *

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)  # 創建socket客戶端
tcp_client.connect(ip_port)  # 嘗試連結服務器

tcp_client.send('hello'.encode('utf-8'))
tcp_client.send('world'.encode('utf-8'))
tcp_client.send('jamie'.encode('utf-8'))


tcp_client.close()
