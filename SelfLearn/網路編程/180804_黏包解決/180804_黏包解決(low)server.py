from socket import *
import subprocess

ip_port = ('127.0.0.1', 8000)
back_log = 5
buffer_size = 1024

tcp_server = socket(AF_INET, SOCK_STREAM)
tcp_server.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
tcp_server.bind(ip_port)
tcp_server.listen(back_log)

while True:
    conn, addr = tcp_server.accept()
    print('雙向連結為 ', conn)
    print('客戶端地址為 ', addr)

    while True:
        try:
            cmd = conn.recv(buffer_size)
            print('客戶端發來的信息 ', cmd)
            if not cmd: break
            res = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            err = res.stderr.read()
            if err:
                cmd_res = err
            else:
                cmd_res = res.stdout.read()
            if not cmd_res:
                cmd_res = "此指令不會有返回值".encode('BIG5')

            # 解決黏包
            length = len(cmd_res)  # 計算cmd_res長度
            conn.send(str(length).encode('utf-8'))
            ready = conn.recv(buffer_size)
            if ready == b'ready':
                conn.send(cmd_res)

        except Exception:
            break

    conn.close()

tcp_server.close()