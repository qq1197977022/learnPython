import socket
import time


def main():
    serve = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    bind_ip_port = ('', 8080)
    serve.bind(bind_ip_port)
    max_num = int(input('最大未连接数: '))
    serve.listen(max_num)
    for i in range(10):
        print(i)
        time.sleep(1)
    while True:
        rs_socket, client_ip_port = serve.accept()    # 返回可以用于在当前connection收发数据的新的socket 和 当前connection另一端即客户端ip_port
        print(f'{rs_socket}\n\t{ip_port}')
        time.sleep(1)


if __name__ == '__main__':
    main()

