import socket
import multiprocessing
import time
import os


def fun(udp_socket, addr):
    # data = '1:21244:范冰冰:kc-pc:32:我爱你'
    data = f'{os.getpid():-<30}{multiprocessing.current_process().name:=>30}\n' * 30
    bytes_data = bytes(data, encoding='GBK')
    for i in range(2):
        num = udp_socket.sendto(bytes_data, addr)
        # time.sleep(1)   # 为什么在发送前延时报错
        print(num)


def main():
    udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)   # 创建socket实例对象

    info()

    addr = ('192.168.102.2', 8080)  # 配置IP + 端口

    pol = multiprocessing.Pool(10)   # 线程池
    for i in range(1000):
        pol.apply_async(func=fun, args=(udp_socket, addr))  # 添加任务到进程池
    pol.close()    # 关闭线程池, 一旦所有任务完成, 工作进程将退出
    pol.join()    # 等待工作进程结束


def info():    # 获取本机信息
    host_name = socket.gethostname()
    # ip_addr = socket.gethostbyname_ex(host_name)
    ip_addr = socket.gethostbyname(host_name)
    print(f'主机名: {host_name}\t 本机IP: {ip_addr}')


if __name__ == '__main__':
    main()


# 一.本地进程间通信
#   1.队列
#   2.同步
#     1.互斥锁
#     2.条件变量 ~ 模拟锁
#     3.etc...
# 二.网络进程间通信
#   1.
# 三.进程间通信条件
#   1.唯一标识问题
#     1.本地
#       1.PID: 唯一标识进程
#     2.网络
#       1.TCP/IP协议
#         1.IP: 唯一标识网络主机
#         2.传输层协议+端口: 唯一标识进程
#   2.通信协议
# 四.TCP/UPD套接字
#   1.TCP: SOCK_STREAM数据流                                        TCP: 传输控制协议(Transmission Control Protocol)
#     1.可靠: 保证数据不丢失
#   2.UDP: SOCK_DGRAM数据报(datagram)                               UDP: 用户数据报协议(User Datagram Protocol)
#     1.快: 尽最大努力交付, 可能存在数据丢失
#   3.类比
#     1.TCP: 类似打电话
#     2.UDP: 类似写信


# 1.创建UPD客户端流程
#   1.创建客户端套接字
#   2.发送数据
#   3.关闭套接字























































































































