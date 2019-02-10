from socket import *
import struct, pickle
from src import ftp_upload

def conn(ip_port, buffer_size, user, pwd):
    tcp_client = socket(AF_INET, SOCK_STREAM)
    tcp_client.connect(ip_port)
    client_data = {
        'user': user,
        'pwd': pwd
    }
    pickle_client = pickle.dumps(client_data)
    tcp_client.send(pickle_client)  # 帳密認證
    status = tcp_client.recv(buffer_size)
    print(status.decode('utf-8'))
    while True:
        try:
            c_msg = input(">> ").strip()
            if not c_msg: continue
            if c_msg == 'break': break

            if c_msg.startswith('upload'):  # 檔案上傳
                filename = c_msg[6:].strip()  # 檔案名稱
                pickle_data = ftp_upload.upload(filename)  # 經pickle轉換後的檔案字典
                tcp_client.send('upload'.encode('utf-8'))
                tcp_client.send(pickle_data[0])
                tcp_client.send(pickle_data[1])

            else:  # cmd操作
                tcp_client.send(c_msg.encode('utf-8'))
            pack_recv_msg = tcp_client.recv(4)  # pack後的msg長度
            l_recv_msg = struct.unpack('i', pack_recv_msg)[0]  # 真實msg長度

            # 解決黏包
            recv_msg = b''
            recv_length = 0
            while recv_length < l_recv_msg:
                recv_msg += tcp_client.recv(buffer_size)
                recv_length = len(recv_msg)

            print('服務端來的信息： ', recv_msg.decode('BIG5'))
        except Exception as e:
            print(e)
            break

    tcp_client.close()
