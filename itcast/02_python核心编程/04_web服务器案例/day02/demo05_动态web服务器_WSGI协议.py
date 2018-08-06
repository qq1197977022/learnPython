# 一.简介
#   1.早期选择Python架构受制于web服务器, 反之亦然 ~ 强耦合
#   2.Python Web Server Gateway Interface(WSGI) ~ 解耦
#     1.WSGI同时支持服务器和架构, 允许开发者将web框架和web服务器分开, 可以混合匹配web框架和web服务器
#         eg. 可以在Guniconm/Nginx/uWSGI/Waitress上运行Django/Flashk/Pyamid
#     2.支持WSGI协议的web服务器和web框架, 不修改代码即可使其协同工作
#     3.WSGI协议有web服务器支持, web框架允许开发者选择适合的配对, 对于web服务器和框架开发者同样提供方便, 使他们可以专注于自己擅长的领域而不至于相互牵制
#     4.其他语言也有类似借口
#         eg. Java ~ Servlet API, Ruby ~ Rack
#   3.WSGI: Web Server Gateway Interface Web服务器网关接口
# 二.定义WSGI接口
#   1.def application(environ, start_response):
#       start_response('200 OK', [('Content-Type', 'text/html'), ('Date', '2018-4-9')])
#       return 'Hello World'
#
#       environ: 包含HTTP请求信息的dict对象
#       start_response: 发送HTTP响应的函数
#
#       application()函数没有涉及解析HTTP部分, 即把底层web服务器解析部分和应用程序逻辑部分分离, 开发者只需专心一个领域
#   2.application函数由支持WSGI协议的web服务器调用,








