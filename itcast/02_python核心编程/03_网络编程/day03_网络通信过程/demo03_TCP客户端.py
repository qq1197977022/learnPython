import socket


def main():
    client_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)    # 创建TCP socket对象

    server_ip_port = ('192.168.85.1', 8080)    # 服务端IpPort
    client_socket.connect(server_ip_port)    # 连接远程服务器

    while True:
        # 发送数据到服务端
        send_bytes = input('请输入: ').encode('GBK')
        if len(send_bytes) == 0:    # 直接回车, 不输入数据, 表示关闭客户端
            break
        client_socket.send(send_bytes)

        # 接收服务端数据
        recv_bytes = client_socket.recv(1024)
        if len(recv_bytes) == 0:
            print('服务端已关闭连接')
            break
        else:
            print(f'服务端数据: {recv_bytes.decode("GBK")}')

    client_socket.close()


if __name__ == '__main__':
    main()
