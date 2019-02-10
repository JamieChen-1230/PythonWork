# tcp的協議數據不會丟，沒有收完包，下次接收，會繼續上次繼續接收，
# 己端總是在收到ack時才會清除緩衝區內容。數據是可靠的，但是會粘包。
from socket import *
import subprocess

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
        try:  # 非正常斷開處理
            cmd = conn.recv(buffer_size)
            print('客戶端發來的信息 ', cmd)
            if not cmd: break  # 正常斷開處理
            # 執行命令，得到命令結果cmd_res
            res = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdout=subprocess.PIPE, stdin=subprocess.PIPE, stderr=subprocess.PIPE)
            err = res.stderr.read()
            if err:
                cmd_res = err
            else:
                cmd_res = res.stdout.read()
            if not cmd_res:
                cmd_res = "此指令不會有返回值".encode('BIG5')

            conn.send(cmd_res)
        except Exception:  # 當客戶端段開連結後會報錯，所以直接break掉，進入下一個等待連結的循環
            break

    conn.close()

tcp_server.close()