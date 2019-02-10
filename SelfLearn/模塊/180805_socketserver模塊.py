# socketserver分成兩大類：
# ---------server類：處理鏈結---------(Forking：多進程、Threading：多線程)
# BaseServer

# TCPServer(BaseServer)
#   ForkingTCPServer(ForkingMixIn, TCPServer)
#   ThreadingTCPServer(ThreadingMixIn, TCPServer)

# UDPServer(TCPServer)
#   ForkingUDPServer(ForkingMixIn, UDPServer)
#   ThreadingUDPServer(ThreadingMixIn, UDPServer)

# UnixStreamServer(用於Unix)
# UnixDatagramServer(用於Unix)

# ---------request類：處理通信---------
# BaseRequestHandler(一定要自定義handler)
# StreamRequestHandler
# DatagramRequestHandler

