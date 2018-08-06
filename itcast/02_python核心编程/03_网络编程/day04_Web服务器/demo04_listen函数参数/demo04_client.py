import socket


def main():
    # num = int(input('连接数: '))
    # for i in range(num):
    #     client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    #     dst_ip_port = ('127.0.0.1', 8080)
    #     client.connect(dst_ip_port)
    #     print(i)

    count = 0
    while True:
        client = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        dst_ip_port = ('39.107.248.251', 8080)
        client.connect(dst_ip_port)
        count += 1
        print(count)


if __name__ == '__main__':
    main()



