from gevent import socket, monkey, Greenlet
monkey.patch_all()


def service(conn):
    while True:
        rec_byts = conn.recv(1024)
        if len(rec_byts) == 0:
            print(f'客户端{conn.getpeername()}关闭连接')
            conn.close()
            break
        print(rec_byts.decode('GBK'))


def main():
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    bind_ip_port = ('', 8080)
    server.bind(bind_ip_port)
    server.listen(5)

    while True:
        conn, client_ip_port = server.accept()
        print(f'客户端{client_ip_port}建立连接')
        Greenlet.spawn(service, conn)
        # g = Greenlet.spawn(service, conn)
        # g.join()  # 阻塞, 直到当前Greenlet结束或超时


if __name__ == '__main__':
    main()


