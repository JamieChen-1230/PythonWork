import socket
import select

"""
HTTP請求本質，阻塞
"""
# sk = socket.socket()
# """連接"""
# # 默認大部分都是80端口
# sk.connect(("www.baidu.com", 80))  # IO阻塞
# print("連接成功了...")
#
# """發送訊息"""
# sk.send(b"GET / HTTP/1.0\r\nHost: baidu.com\r\n\r\n")
#
# """等待服務端響應"""
# # 最多接收8096大小的資料
# data = sk.recv(8096)  # IO阻塞
# print(data)
#
# """關閉連接"""
# sk.close()


"""
HTTP請求本質，非阻塞
"""
# sk = socket.socket()
# """設定為非阻塞"""
# sk.setblocking(False)
# try:
#     """連接"""
#     # 默認大部分都是80端口
#     sk.connect(("www.baidu.com", 80))
#     print("連接成功了...")
# except BlockingIOError as e:
#     print(e)
#
# """發送訊息"""
# sk.send(b"GET / HTTP/1.0\r\nHost: baidu.com\r\n\r\n")
#
# """等待服務端響應"""
# # 最多接收8096大小的資料
# data = sk.recv(8096)
# print(data)
#
# """關閉連接"""
# sk.close()


"""
異步IO模塊本質
"""
class HttpResponse:
    def __init__(self, recv_data):
        self.recv_data = recv_data
        self.header_dict = {}
        self.body = None
        self.initialize()

    def initialize(self):
        """把回傳資料切分為響應頭和響應體"""
        headers, body = self.recv_data.split(b"\r\n\r\n", 1)  # 切分第一個b"\r\n\r\n"
        self.body = body
        header_list = headers.split(b"\r\n")

        for h in header_list:
            h_str = str(h, encoding="utf-8")
            v = h_str.split(":", 1)
            if len(v) == 2:
                self.header_dict[v[0]] = v[1]


class HttpRequest:
    def __init__(self, sk, host, callback):
        self.socket = sk
        self.host = host
        self.callback = callback

    def fileno(self):
        return self.socket.fileno()


class AsyncRequest:
    def __init__(self):
        self.conn = []
        self.connection = []  # 用於檢測是否已經連接成功，若在connection中表示尚未連接成功

    def add_request(self, host, callback):
        try:
            """連接"""
            sk = socket.socket()
            sk.setblocking(False)
            sk.connect((host, 80,))
        except BlockingIOError as e:
            pass
        request = HttpRequest(sk, host, callback)
        self.conn.append(request)
        self.connection.append(request)

    def run(self):
        while True:
            # select參數： 對象須有fileno方法，並返回一個文件描述符
            r_list, w_list, e_list = select.select(self.conn, self.connection, [], 0.05)
            for w in w_list:
                # w是HttpRequest對象
                # 只要能在w_list中讀取到，表示此socket和服務端已經連接成功
                print(w.host, "連接成功了...")
                tql = "GET / HTTP/1.0\r\nHost: %s\r\n\r\n" % (w.host, )
                """發數據"""
                w.socket.send(bytes(tql, encoding="utf-8"))
                """發送數據後，表示不須再對他進行監聽，故移除"""
                self.connection.remove(w)

            for r in r_list:
                # r是HttpRequest對象
                # 只要能在r_list中讀取到，表示有人(服務端)給此socket發送數據了

                recv_data = bytes()
                while True:  # 因為有可能數據大於8096
                    try:  # 數據讀取完畢則報錯
                        """接收數據"""
                        chunk = r.socket.recv(8096)
                        recv_data += chunk
                    except Exception as e:
                        break
                print(r.host, "有數據返回了")

                """處理接收數據"""
                response = HttpResponse(recv_data)
                """調用各自的回調函數"""
                r.callback(response)

                """接收到數據後，表示這次連接已結束，不須再對他進行監聽，故close掉且移除"""
                r.socket.close()
                self.conn.remove(r)

            if len(self.conn) == 0:
                """表示全部請求都已完成，故斷開死循環"""
                break


def f1(data):
    print("保存到文件", data.header_dict)


def f2(data):
    print("保存到數據庫", data.header_dict)


url_list = [
    {"host": "www.baidu.com", "callback": f1},
    {"host": "www.google.com", "callback": f2},
    {"host": "www.youtube.com", "callback": f1},
]

req = AsyncRequest()
for item in url_list:
    req.add_request(item["host"], item["callback"])

req.run()
