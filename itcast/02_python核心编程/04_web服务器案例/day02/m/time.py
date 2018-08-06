import time
# import datetime
# import os


def application(req_dic, res_fun):    # 返回响应体
    print(f'HTTP请求信息: {req_dic}')
    # res_start_line = 'HTTP/1.1 200 OK\r\n'
    res_status = '200 OK'
    res_headers = [
        ('Content-Type', 'text/plain')
    ]

    res_fun(res_status, res_headers)  # 构造响应起始行 和 响应头

    # os.system('notepad')  # 备忘, 脚本hack深入...
    res_body = time.ctime()  # Sun May 13 08:39:46 2018
    # res_body = datetime.datetime.now()  # 2018-05-13 08:39:07.981812
    return res_body





