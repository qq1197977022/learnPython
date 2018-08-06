def application(req_dic, res_fun):
    print(f'HTTP请求信息: {req_dic}')

    status = '200 OK'
    res_headers = [
        ('Content-Type', 'text/plain')
    ]
    res_fun(status, res_headers)

    res_body = 'Hello World'
    return res_body








