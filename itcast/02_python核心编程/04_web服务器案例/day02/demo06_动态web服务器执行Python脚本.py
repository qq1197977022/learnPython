import socket
import threading
import re
import sys


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

    def _res_fun(self, res_status, res_headers):
        res_start_line = f'HTTP/1.1 {res_status}\r\n'

        headers = ''
        for k, v in res_headers:
            headers += f'{k}:{v}\r\n'
        else:
            self.res_startLine_headers = f'{res_start_line}{headers}'

    def _handle(self, conn):
        recv_byts = conn.recv(1024)
        # print(f'{"request":=^30}\n{recv_byts.decode()}')  # 请求

        module_path = 'D:\\workspace\\python\\itcast\\02_python核心编程\\04_web服务器案例\\day02\\m\\'
        flag = True
        try:
            reg = re.compile(r'(\w*) /?(\w*\.*[A-z]*) HTTP/1.1')
            method = reg.match(recv_byts.decode()).group(1)
            req_file = reg.match(recv_byts.decode()).group(2)
        except AttributeError:    # 正则匹配失败
            req_file = 'index.html'
            with open(f'html/index.html', 'rt', encoding='GB2312') as f:
                res_body = f.read()
        else:   # 正则匹配成功
            if req_file == '' or req_file == 'index.html':
                with open('html/index.html', 'rt', encoding='GB2312') as f:
                    res_body = f.read()
            elif req_file.endswith('.py'):
                sys.path.insert(1, module_path)    # 添加模块搜索路径
                try:
                    m = __import__(req_file[:-3])
                    print(f'导入模块------>{m}')
                except ModuleNotFoundError:
                    res_body = f'模块{req_file} Not Found...'
                else:
                    req_dic = {
                        "PATH_INFO": req_file,
                        "METHOD": method
                    }
                    res_body = m.application(req_dic, self._res_fun)
                    res_headers = self.res_startLine_headers
                    flag = False
            else:
                res_body = f'{req_file} Not Found...\r\n'
        finally:
            print(f'请求文件------------------------------------>{repr(req_file)}')
            if flag:
                res_start_line = 'HTTP/1.1 200 OK\r\n'
                res_headers = 'Date: Wed, 09 May 2018 00:56:26 GMT\r\n' \
                              'Server: BWS/1.1\r\n'
                res = f'{res_start_line}{res_headers}\r\n{res_body}\r\n'
            else:
                res = f'{res_headers}\r\n{res_body}'

            conn.send(res.encode('GB2312'))
            conn.close()
            # print(f'{"response":*^30}\n{res}')    # 响应


def main():
    server = Server(('', 80))
    server.start()


if __name__ == '__main__':
    main()


# Note: Chrome会发送多次请求, MSEdge不会





















































