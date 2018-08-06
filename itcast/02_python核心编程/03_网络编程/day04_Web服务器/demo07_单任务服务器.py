import socket


def serve(rs_socket):
    while True:
        recv_bytes = rs_socket.recv(1024)
        if len(recv_bytes) == 0:
            print('客户端已关闭连接')
            break
        print(recv_bytes.decode('GBK'))

    rs_socket.close()


def main():
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    bind_ip_port = ('192.168.85.1', 8080)
    server_socket.bind(bind_ip_port)

    server_socket.listen(5)    # 启动一个服务以接受connection

    while True:
        rs_socket, client_ip_port = server_socket.accept()
        print(f'接受{client_ip_port}连接成功')
        serve(rs_socket)


if __name__ == '__main__':
    main()


# 多任务版本参见: D:\workspace\python\itcast\02_python核心编程\03_网络编程\day03_网络通信过程\demo04_TCP多任务服务器.py

