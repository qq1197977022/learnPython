import socket
import threading
import re


class Server(object):
    """注释"""
    def __init__(self, ip_port):
        self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.sock.bind(ip_port)

    def start(self):
        self.sock.listen(5)
        while True:
            conn, client_ip_port = self.sock.accept()
            print(f'{client_ip_port}已连接')
            t = threading.Thread(target=self._handle, args=(conn,))
            t.start()
            t.join()

    def _handle(self, conn):
        recv_byts = conn.recv(1024)
        print(f'{"request":=^30}\n{recv_byts.decode()}')

        try:
            try:
                reg = re.compile(r'GET /(\w*\.*[A-z]*) HTTP/1.1')
                req_file = reg.match(recv_byts.decode()).group(1)
            except AttributeError:
                print('正则匹配失败')
                req_file = ''
            finally:
                if req_file == '':
                    req_file = 'index.html'

                print(f'请求页面{req_file}')

            with open(f'../day01/html/{req_file}', 'rt', encoding='utf-8') as f:

                res_start_line = 'HTTP/1.1 200 OK\r\n'
                res_header = 'Date: Wed, 09 May 2018 00:56:26 GMT\r\n' \
                             'Server: BWS/1.1\r\n'
                res_body = f.read()

        except :
            res_start_line = 'HTTP/1.1 302 Found\r\n'
            res_header = 'Date: Wed, 09 May 2018 00:56:26 GMT\r\n' \
                         'Server: BWS/1.1\r\n'
            res_body = f'{req_file} Not Found...\r\n'   # 编码后解码, 保持和200读文件字节模式res_body保持一致
        finally:
            res = f'{res_start_line}{res_header}\r\n{res_body}\r\n'
            conn.send(res.encode())
            conn.close()
            print(f'{"response":*^30}\n{res}')


def main():
    server = Server(('', 80))
    server.start()


if __name__ == '__main__':
    main()


# Note: 由于浏览器实习那原因导致可能发送多次请求, 使用NetAssist可以避免此现象






