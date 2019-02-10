import subprocess
import struct
import socketserver

ip_port = ('127.0.0.1', 8000)
buffer_size = 1024

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn is ', self.request)  # conn
        print('addr is ', self.client_address)  # addr

        while True:
            try:
                cmd = self.request.recv(buffer_size)
                print("收到%s客戶端信息 %s" % (self.client_address, cmd))
                if not cmd: break
                res = subprocess.Popen(cmd.decode('utf-8'), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                err = res.stderr.read()
                if err:
                    cmd_res = err
                else:
                    cmd_res = res.stdout.read()
                if not cmd_res:
                    cmd_res = "此指令不會有返回值".encode('BIG5')

                # 解決黏包
                length = len(cmd_res)  # 計算cmd_res長度
                pack_length = struct.pack('i', length)  # 自定義header

                self.request.send(pack_length)
                self.request.send(cmd_res)
            except Exception:
                break

if __name__ == "__main__":
    s = socketserver.ThreadingTCPServer(ip_port, MyServer)  # 多線程，每來一個客戶端創一個實例
    s.serve_forever()  # 服務器循環(連結循環)


