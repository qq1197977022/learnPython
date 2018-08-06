import socket


server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)    # 创建TCP socket对象

# 绑定IpPort
bind_ip_port = ('192.168.85.1', 8080)
server_socket.bind(bind_ip_port)

# 监听
print('启动一个服务监听connection')
server_socket.listen(5)  # 参数设定系统拒绝新的connection前, 最大未接收链接数

# 接受socket
rs_socket, client_ip_port = server_socket.accept()
print('接收到connection', rs_socket, client_ip_port, sep='\n')

# 接收客户端数据
recv_data_bytes = rs_socket.recv(1024)
print(recv_data_bytes.decode('GBK'))

# 发送数据到客户端
send_data_bytes = '切, 不约!'.encode('GBK')
rs_socket.send(send_data_bytes)

# 关闭套接字, 释放资源
rs_socket.close()
server_socket.close()




























































