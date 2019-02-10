import socketserver, subprocess, struct, pickle, os
from src import ftp_upload
from conf import setting

def conn(ip_port, buffer_size):
    class Myserver(socketserver.BaseRequestHandler):
        def handle(self):
            print('conn is ', self.request)  # conn
            print('addr is ', self.client_address)  # addr
            # 帳密認證
            pickle_client = self.request.recv(buffer_size)
            client_data = pickle.loads(pickle_client)
            account = setting.conf_path + os.sep + 'account.txt'
            with open(account, 'r') as f:
                account_list = eval(f.read())
            log_in = False
            for i in account_list:
                if client_data['user'] == i['user'] and client_data['pwd'] == i['pwd']:
                    log_in = True

            if log_in:
                status = '%s登入成功' % client_data['user']
                self.request.send(status.encode('utf-8'))
                while True:
                    # try:
                        recv_msg = self.request.recv(buffer_size)
                        print("【%s】客戶端來的信息：%s" % (client_data['user'], recv_msg))
                        if recv_msg.startswith('upload'.encode('utf-8')):  # 檔案上傳
                            pack_pickle_data = self.request.recv(4)
                            l_pickle_data = struct.unpack('i', pack_pickle_data)[0]
                            # print(l_pickle_data)
                            # 解決黏包
                            pickle_data = b''
                            recv_length = 0
                            while recv_length < l_pickle_data:
                                # print('%.1f %%' % (recv_length/l_pickle_data*100))
                                # percent = str(int(recv_length / l_pickle_data * 100))
                                # self.request.send(percent.encode('utf-8'))
                                pickle_data += self.request.recv(buffer_size)  # 經pickle轉換後的檔案字典
                                recv_length = len(pickle_data)
                            data_dic = pickle.loads(pickle_data)  # 檔案字典
                            ftp_upload.upload(data_dic['filename'], data_dic['data'])  # 上傳
                            s_msg = "上傳成功".encode('BIG5')
                        else:  # cmd操作
                            cmd_res = subprocess.Popen(recv_msg.decode('utf-8'), shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            cmd_err = cmd_res.stderr.read()
                            if cmd_err:
                                s_msg = cmd_err
                            else:
                                s_msg = cmd_res.stdout.read()
                            if not s_msg:
                                s_msg = "指令成功".encode('BIG5')

                        # 解決黏包
                        l_s_msg = len(s_msg)
                        pack_msg = struct.pack('i', l_s_msg)
                        self.request.send(pack_msg)
                        self.request.sendall(s_msg)
                    # except Exception as e:
                    #     print(e)
                    #     break
            else:
                self.request.send('帳號錯誤'.encode('utf-8'))
                print('帳號錯誤')

    s = socketserver.ThreadingTCPServer(ip_port, Myserver)
    s.serve_forever()


