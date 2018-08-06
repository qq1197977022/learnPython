# Bind the socket to a local address
#   1.IP socket: address is a pair(host, port)
#       1.如果IP不明确指定, 则为本机任意网卡IP地址
#   2.raw packet socket: address is a tuple(ifname, proto, [, pkttype [,hatype]])
#

# 网络程序每次启动, 操作系统都会为其分配唯一随机端口
# 服务端程序一般需要绑定唯一不变端口

# 单工: 单向
#   eg. 收音机
# 半双工: 双向但非同时
#   eg. 对讲机
# 全双工: 双向且同时
#   eg. 电话
import socket


def main():
    udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
    udp_socket.bind(('192.168.102.2', 8080))
    msg = udp_socket.recv(2048)
    print(msg.decode('GBK'))


if __name__ == '__main__':
    main()


