import socket
import multiprocessing


def handle(conn):
    req_byts = conn.recv(1024)
    # print(req_byts.partition(b'\r\n')[0])
    # print(f'splite: {req_byts.split()}')

    print(f'原始请求数据:\n{req_byts}')
    req_str = req_byts.decode('GBK')
    print(f'请求数据:\n{req_str}')

    # 构造响应
    # 1.起始行
    res_start_line = 'HTTP/1.1 200 OK\r\n'
    # 2.响应头
    res_header = 'server: My Server\r\n'\
                 'Date: Fri, 27 Apr 2018 01:18:19 GMT\r\n'
    # 3.响应体
    res_body = '<h1>Hello World</h1>'
    res = f'{res_start_line}{res_header}\r\n{res_body}'
    conn.send(res.encode())
    print(f'响应:\n{res}')
    conn.close()


def main():
    while True:
        server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        bind_ip_port = ('', 8000)
        server.bind(bind_ip_port)

        server.listen(5)    # 启动一个服务以接受connection
        conn, client_ip_port = server.accept()
        print(f'{client_ip_port}TCP连接建立')
        p = multiprocessing.Process(target=handle, args=(conn,))
        p.start()

        conn.close()
    # server.close()


if __name__ == '__main__':
    main()























