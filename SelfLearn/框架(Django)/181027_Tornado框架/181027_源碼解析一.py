import tornado.ioloop
import tornado.web


class MainHandler(tornado.web.RequestHandler):
    def get(self, *args):
        self.write("Hello World")


class LoginHandler(tornado.web.RequestHandler):
    def get(self, *args):
        # self.write("Hello World")
        self.render("login.html")  # 渲染頁面

    def post(self, *args, **kwargs):
        v = self.get_argument("user")
        print(v)
        self.redirect("/index")  # 跳轉

# 配置文件
settings = {
    "template_path": "templates",
    "static_path": "static",  # 指的是服務端的static目錄
    "static_url_prefix": "/stc/",  # 頁面上使用的前綴別名，默認為/static/

}

# Application對象封裝了路由信息、配置信息
application = tornado.web.Application([
    (r"/login", LoginHandler),
    (r"/index", MainHandler),
], **settings)

if __name__ == '__main__':
    # 創建socket對象 [socket, ]
    # s = socket.socket()
    # inputs = [s, ]
    application.listen(8888)

    # 運行
    # r, w, e = select.select(inputs)
    tornado.ioloop.IOLoop.current().start()
