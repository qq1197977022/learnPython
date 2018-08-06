import socket
import threading
import re


class Server(object):
    """注释"""
    def __init__(self, ip_port, app_obj):
        self.sock = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
        self.sock.bind(ip_port)
        self.app = app_obj

    def start(self):
        self.sock.listen(5)
        while True:
            conn, client_ip_port = self.sock.accept()
            print(f'{client_ip_port}已连接')
            t = threading.Thread(target=self._handle, args=(conn,))
            t.start()
            t.join()

    def _res_fun(self, res_status, res_headers):
        res_start_line = f'HTTP/1.1 {res_status}\r\n'

        headers = ''
        for k, v in res_headers:
            headers += f'{k}:{v}\r\n'
        else:
            self.res_start_line = res_start_line
            self.res_headers = headers

    def _handle(self, conn):
        recv_byts = conn.recv(1024)
        # print(f'{"request":=^30}\n{recv_byts.decode()}')  # 请求

        try:
            reg = re.compile(r'(\w*) /((?:\w*/?)*\.*[A-z]*) HTTP/1.1')
            req_method = reg.match(recv_byts.decode()).group(1)
            req_uri = reg.match(recv_byts.decode()).group(2)
            print(f'req_method = {repr(req_method)}\t req_uri = {repr(req_uri)}')
        except AttributeError:
            req_uri = 'req_uri'
            req_method = 'GET'
            print('-------------->正则匹配错误...')
        finally:
            req_dic = {
                'PATH_INFO': req_uri,
                'METHOD': req_method
            }
            res_body = self.app(req_dic, self._res_fun)

            res = f'{self.res_start_line}{self.res_headers}\r\n{res_body}\r\n'

            conn.send(res.encode('GB2312'))
            conn.close()
            # print(f'{"response":*^30}\n{res}')    # 响应


# Note: Chrome会发送多次请求, MSEdge不会





















































