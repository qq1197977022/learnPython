# 思路: 改变阻塞部分为非阻塞
import socket


def main():
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server.setblocking(False)  # 设置非阻塞

    bind_ip_port = ('10.106.20.67', 8080)
    server.bind(bind_ip_port)

    server.listen(5)

    socket_list = []  # 用于收发数据的socket队列

    while True:
        # 接受连接
        try:
            conn = server.accept()
        except:  # 忽略所有异常
            pass
        else:
            conn[0].setblocking(False)  # 设置非阻塞
            socket_list.append(conn)

        # 轮询接收数据
        for conn in socket_list:
            try:
                recv_bytes = conn[0].recv(1024)
            except:  # 忽略所有异常
                pass
            else:
                if len(recv_bytes) == 0:
                    print(f'客户端{conn[1]}已关闭连接')
                    conn[0].close()
                    socket_list.remove(conn[0])
                else:
                    print(recv_bytes.decode('GBK'))


if __name__ == '__main__':
    main()














