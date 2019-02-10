from socket import *

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

tcp_client = socket(AF_INET, SOCK_STREAM)  # 創建socket客戶端
tcp_client.connect(ip_port)  # 嘗試連結服務器

tcp_client.send('helloworldjamie'.encode('utf-8'))



tcp_client.close()
