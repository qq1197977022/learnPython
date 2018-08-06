import time
from MyWebServer import Server


class Application(object):
    """注释"""
    def __init__(self, static_uris, dynamic_uris):
        self.static_uris = static_uris  # 静态路由表
        self.dynamic_uris = dynamic_uris  # 动态路由表

    def __call__(self, req_dic, res_fun):
        req_uri = req_dic.get('PATH_INFO', '')  # 默认req_uri = ''/index.html
        res_body = _uris(self.static_uris, self.dynamic_uris, req_uri, req_dic, res_fun)
        return res_body


def _uris(static_uris, dynamic_uris, req_uri, req_dic, res_fun):  # 路由分发
    if req_uri.startswith('static'):
        uris = static_uris
        req_uri = req_uri[7:]
    else:
        uris = dynamic_uris

    for uri, handler in uris:
        if uri == req_uri:
            res_body = handler(req_dic, res_fun)
            return res_body
    else:
        res_body = e(req_dic, res_fun, req_uri)
        return res_body


def index(req_dic, res_fun):
    with open('../html/index.html') as f:
        status = '200 OK'
        res_headers = [
            ('Content-Type', 'text/html'),
            ('Server', 'MyServer')
        ]
        res_fun(status, res_headers)

        res_body = f.read()
    return res_body


def ctime(req_dic, res_fun):
    status = '200 OK'
    res_headers = [
        ('Content-Type', 'text/plain'),
        ('Server', 'MyServer')
    ]
    res_fun(status, res_headers)

    res_body = time.ctime()
    return res_body


def say_hello(req_dic, res_fun):
    status = '200 OK'
    res_headers = [
        ('Content-Type', 'text/plain'),
        ('Server', 'MyServer')
    ]
    res_fun(status, res_headers)

    res_body = 'HelloWorld'
    return res_body


def e(req_dic, res_fun, req_uri):
    status = '404 Not Found'
    res_headers = [
        ('Content-Type', 'text/plain'),
        ('Server', 'MyServer')
    ]
    res_fun(status, res_headers)

    res_body = f'{repr(req_uri)} Not Found...'
    return res_body


def main():
    static_uris = [
        ('', index),
        ('index', index),
        ('index.html', index)
    ]
    dynamic_uris = [  # 路由表
        ('ctime', ctime),
        ('sayHello', say_hello)
    ]
    app = Application(static_uris, dynamic_uris)
    server = Server(('', 80), app)
    server.start()


if __name__ == '__main__':
    main()
































