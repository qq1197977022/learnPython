import select
import socket

server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
serve_ip_port = ('', 8080)
server.bind(serve_ip_port)

server.listen(5)    # 启动一个服务以接受connection ~ 监听

epoll = select.epoll()
epoll.register(server.fileno(), select.EPOLLIN|select.EPOLLET)  # 在epoll对象中注册server socket文件描述符, 设置事件掩码为 可读 + 水平/条件触发

rsSockFd_rsSock = {}    # 记录客户端在服务端标识
rsSockFd_clientIpPort = {}

flag = False    # 远程关机标识
while True:
    epoll_lis = epoll.poll()    # 等待事件
    for fd, event in epoll_lis:
        if fd == server.fileno():
            rs_sock, client_ip_port = server.accept()   # 接受connection ~ TCP连接建立
            epoll.register(rs_sock.fileno(), select.EPOLLIN | select.EPOLLET)    # 在epoll对象中注册rs_sock socket文件描述符, 设置事件掩码为 可读 + 水平/条件触发
            print(f'客户端{client_ip_port}已连接')

            rsSockFd_rsSock[rs_sock.fileno()] = rs_sock    # 在服务端标识客户端
            rsSockFd_clientIpPort[rs_sock.fileno()] = client_ip_port
        elif event == select.EPOLLIN:
            rcvByts = rsSockFd_rsSock[fd].recv(1024)    # 接收数据

            if len(rcvByts) == 0:
                epoll.unregister(fd)    # 从epoll对象中移除文件描述符 ~ 注销
                rsSockFd_rsSock[fd].close()
                print(f'客户端{rsSockFd_clientIpPort[fd]}关闭连接')

                rsSockFd_rsSock.pop(fd)    # 删除客户端标识记录
                rsSockFd_clientIpPort.pop(fd)
                continue
            else:
                data = rcvByts.decode('GBK')
                print(data)
                if data == 'exit':
                    flag = True
                    print(f'客户端{rsSockFd_clientIpPort[fd]}远程关闭服务器')

    if flag:
        break

server.close()


# Edge and Level Trigger
#   1.Edge Triger: 边缘触发 ~ 仅状态变化时, 触发一次
#   2.Level Trigger: 水平/条件触发 ~ 条件满足, 反复触发
#     1.若有数据没有被获取, 内核不断通知, 直到数据全部被获取, 即条件不满足


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

#   4.select--改进: 无上限-->poll--改进: 事件通知机制-->epoll

# 重点: IO多路复用模型!!!!!!!! ~~~~~~~~~~ 待理解


# 其他知识
# 注: fd: an small integer corresponding to a file that has been opened by current process
# 一.os.open()
# 	1.返回新打开文件的fd(文件描述符), 该fd is non-inheritable
# 	2.该函数适用于低级I/O
# 	3.对于通常用法, 内置函数open()返回带有read()和write()等方法的文件对象
# 	4.使用fdopen()函数可将fd包装到文件对象
# 二.os.fdopen()
# 	1.返回连接到指定fd的文件对象
# 	2.该函数是内置函数open()的别名函数
# 	3.唯一的区别是: 该函数首参是一个fd
# 三.可以通过sys.stdout = open(xxx), 指向标准输出的文件描述符的文件
# 卧槽...对程序设计有了更深的认识 ~ 各种组合...配合...关联













