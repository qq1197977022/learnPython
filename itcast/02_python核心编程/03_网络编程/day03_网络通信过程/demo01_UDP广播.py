import socket


udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
dst_ip_port = ('192.168.159.255', 8080)
# bind_ip_port = ('192.168.159.1', 8080)
# udp_socket.bind(bind_ip_port)
# IPV4有两个特殊格式可用于代替host address
#   1.空串: INADDR_ANY
#   2.'<broadcast>': INADDR_BROADCAST, 不支持IPV6

udp_socket.setsockopt(socket.SOL_SOCKET, socket.SO_BROADCAST, 1)    # 设置socket选项

send_data = '你好啊'
udp_socket.sendto(send_data.encode(encoding='GBK'), dst_ip_port)

# recv_data_bytes = udp_socket.recv(1024)
# print(recv_data_bytes.decode('GBK'))

udp_socket.close()

# 1.只有UDP有广播, TCP没有, 协议本身特点决定
# 2.网络通信
#   1.单播: 一对一
#   2.多播: 一对多
#   4.广播: 一对所有
# 3.广播并不是给每个人都发一份, 而是只发一份到交换机, 由交换机分发


# 问题
#   1.本机能收到虚拟机广播包, 但虚拟机收不到本机广播包 ~ NAT模式






























































