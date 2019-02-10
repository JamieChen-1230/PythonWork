import socketserver

class MyServer(socketserver.BaseRequestHandler):
    def handle(self):
        print('conn is ', self.request)  # conn
        print('addr is ', self.client_address)  # addr

        while True:  # 通訊循環
            try:
                # 收
                data = self.request.recv(1024)
                if not data: break
                print("收到%s客戶端信息 %s"% (self.client_address, data))
                # 發
                self.request.sendall(data.upper())
            except Exception as e:
                print(e)
                break

if __name__ == "__main__":
    s = socketserver.ThreadingTCPServer(('127.0.0.1', 8000), MyServer)  # 多線程，每來一個客戶端創一個實例
    s.serve_forever()  # 服務器循環(連結循環)
