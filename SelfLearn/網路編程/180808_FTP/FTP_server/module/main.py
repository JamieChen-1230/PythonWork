import optparse, socketserver
from conf import settings
from module import server

class ArgvHandler:

    def __init__(self):
        self.parse = optparse.OptionParser()
        # cmd中輸入上述有定義的格式資料會放進options，產生類型為一個對象
        # 而剩下無定義的則放入args
        options, args = self.parse.parse_args()

        self.verify_args(options, args)

    def verify_args(self, options, args):
        cmd = args[0]
        # 使用反射函數
        # 而不要使用if cmd=='start':等(因為以後不好維護)
        if hasattr(self, cmd):  # 判斷對象是否有該屬性(如果self.cmd_first()存在回傳True)
            func = getattr(self, cmd)  # 找出該對象的方法並賦給func
            func()

    def start(self):
        print('----server is working----')
        # 以後這種需要調整的變數(settings.IP, settings.PORT)都寫到settings
        s = socketserver.ThreadingTCPServer((settings.IP, settings.PORT), server.ServerHandler)
        s.serve_forever()
