import threading
import socket
import time


def recv(udp_socket):
    bind_ip_port = ('192.168.102.2', 8080)
    udp_socket.bind(bind_ip_port)  # 绑定
    while True:
        recv_data = udp_socket.recv(1024)   # 有数据接收, 无数据则阻塞
        print(f'接收{recv_data.decode("GBK"):->60}')


def send(udp_socket):
    while True:
        send_data = input('请输入: ')
        dst_ip_port = ('192.168.102.2', 8080)
        udp_socket.sendto(send_data.encode('GBK'), dst_ip_port)


def main():
    udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)   # 创建UDP SOCKET 对象

    send_thread = threading.Thread(target=send, args=(udp_socket,))    # 发送线程
    send_thread.start()

    time.sleep(2)
    recv_thread = threading.Thread(target=recv, args=(udp_socket,))    # 接收线程
    recv_thread.start()

    recv_thread.join()  # 阻塞
    send_thread.join()  # 阻塞


if __name__ == '__main__':
    main()





