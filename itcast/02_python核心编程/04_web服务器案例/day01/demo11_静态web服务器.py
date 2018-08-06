import socket
import threading
import re


def handle(conn):
    recv_byts = conn.recv(1024)
    print(f'{"request:":-^60}\n{recv_byts.decode()}')

    # 构造response
    req_file_ame = re.match(r'\w+ +(/[^ ]*) ', recv_byts.partition(b'\r\n')[0].decode()).group(1)
    try:
        with open(f'html{req_file_ame}', 'rb') as f:   # 以字节模式读取更通用
            res_start_line = 'HTTP/1.1 200 OK'
            res_header = 'server: My Server\r\n' \
                         'Date: Fri, 27 Apr 2018 01:18:19 GMT\r\n'
            res_body = f.read().decode()
    except Exception:    # 匹配任意异常错误
        res_start_line = 'HTTP/1.1 404 Nt Found'
        res_header = 'server: My Server\r\n' \
                     'Date: Fri, 27 Apr 2018 01:18:19 GMT\r\n'
        res_body = f'{req_file_ame}不存在'

    res = f'{res_start_line}{res_header}\r\n{res_body}\r\n'
    print(f'{"response:":-^60}\n{res}')
    conn.send(res.encode(encoding='UTF-8'))
    conn.close()


def main():
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    bind_ip_port = ('', 80)
    server.bind(bind_ip_port)
    server.listen(5)

    while True:
        conn, client_ip_port = server.accept()

        t = threading.Thread(target=handle, args=(conn,))
        t.start()
        t.join()

        conn.close()


if __name__ == '__main__':
    main()



