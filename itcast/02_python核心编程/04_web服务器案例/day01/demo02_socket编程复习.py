import socket
server = socket.socket()    # 默认: family=AF_INET, type=SOCK_STREAM
server.bind(('', 8080))
server.listen(5)
print(server.accept())

# socket等是操作系统对网络通信协议的实现, 但并非所有操作系统都提供网络通信功能
#   eg. 早期网络不发达, 计算机主要用于计算

