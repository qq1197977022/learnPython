# 用多线程实现多任务服务器

import socket
import threading
# import multiprocessing


def serve(rs_socket):
    while True:
        # 接收客户端数据
        recv_bytes = rs_socket.recv(1024)
        if len(recv_bytes) == 0:
            print('客户端已关闭连接')
            break
        print(f'客户端数据: {recv_bytes.decode("GBK")}')    # 输出

        # 发送数据到客户端
        send_data_bytes = input('请输入: ')
        if len(send_data_bytes) == 0:   # 直接回车, 不输入数据, 表示关闭服务端
            break
        rs_socket.send(send_data_bytes.encode('GBK'))

    rs_socket.close()    # 关闭套接字, 释放资源


def main():
    server_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)    # 创建服务端socket对象

    # 绑定ip_port
    bind_ip_port = ('192.168.85.1', 8080)
    server_socket.bind(bind_ip_port)

    server_socket.listen(5)    # 启动一个服务以接受connection

    while True:
        # 接受connection
        rs_socket, client_ip_port = server_socket.accept()
        print(f'已接受连接: {rs_socket}"\n\t"{client_ip_port}')

        # 多线/进程
        t = threading.Thread(target=serve, args=(rs_socket,))
        t.start()
        # p = multiprocessing.Process(target=serve, args=(rs_socket,))
        # p.start()

    # server_socket.close()


if __name__ == '__main__':
    main()


# 问题:
#   1.recv函数不接收空?
#       现象: 直接回车, send函数执行(从输出调试来看, 数据确实已发送), 但另一端不会接收到任何数据, 导致客户端/服务端均阻塞在recv函数
#   2.当socket关闭, recv返回长度为0的数据






















