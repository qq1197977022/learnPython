import socket
import time

udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_socket.bind(('192.168.102.2', 8080))
while True:
    recvf_data = udp_socket.recvfrom(1024)
    lst = list(recvf_data)  # 元组转列表
    lst[0] = lst[0].decode('GBK')   # 解码
    print(lst)

    udp_socket.sendto(recvf_data[0], recvf_data[1])    # echo

    time.sleep(1)


# 1.echo服务器: 回射服务器
#   eg. ping回显













