import socket
import select


def main():
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)

    serve_ip_port = ('127.0.0.1', 8080)
    server.bind(serve_ip_port)

    server.listen(5)

    rlist = [server]
    wlist = []
    xlist = []
    flag = False    # 客户端远程关闭服务器标识
    while True:
        readable, writeable, xable = select.select(rlist, wlist, xlist)    # win下不允许3个空序列
        print('--------------------------------------------------------------------------------辅助查看执行过程')
        for sock_obj in readable:
            if sock_obj == server:   # 监听到连接: 接受, 追加
                rs_sock, client_ip_port = sock_obj.accept()   # 接受连接
                rlist.append(rs_sock)   # 尾追加
                print(f'客户端{client_ip_port}已连接')
                print(rs_sock)
            else:   # accept返回的用于收发数据的socket: 数据收发
                recv_bytes = sock_obj.recv(1024)    # 接收数据
                if len(recv_bytes) == 0:    # 客户端关闭连接
                    print(f'客户端{sock_obj.getpeername()}关闭连接')   # 返回当前套接字已连接的远程地址
                    sock_obj.close()    # 关闭套接字, 释放资源
                    rlist.remove(sock_obj)  # 从rlist中移除
                    continue
                data = recv_bytes.decode('GBK')
                print(f'\t客户端{sock_obj.getpeername()[1]}: {data}')
                if data == 'exit':
                    flag = True
        if flag:
            print(f'客户端{sock_obj.getpeername()}远程关闭服务器')    # 返回当前套接字已连接的远程地址
            break
    server.close()  # 不必理会, pycharm错误; 解决办法: 不用else, 直接裸奔在while循环外即可


if __name__ == '__main__':
    main()


# IO多路复用模型中, 常用的有select和epoll模型

#   1.select: 确定一个或多个套接字的状态 ~ 可读/写性及错误状态信息
#     1.系统接口, 高效
#     2.优点: 跨平台 ~ 几乎所有平台都支持
#     3.缺点
#       1.上限: 单进程可监视文件描述符数存在上限
#         1.linux: 32位~1024, 64位~2048
#         2.采用轮询法检测socket状态, 效率低

#   2.poll: 和select一样, 但无上限

#   3.epoll: 和poll一样, 但采用事件通知机制而不是用轮询法


# 重点: IO多路复用模型!!!!!!!! ~~~~~~~~~~ 待理解




























