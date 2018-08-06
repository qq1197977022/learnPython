# 一.URI: uniform resource identifier(统一资源标识符)
#   1.URL: uniform resource locator(统一资源定位符)
#     eg.https://www.baidu.com:80/index.html
#       1.http: HTTP协议
#       2.www.baidu.com:80: 主机
#       3.index.html: 资源
#   2.URN: Uniform Resource Name(统一资源名称)
#     eg. 图书馆管理员: 告诉其书名, 可得到该书具体位置
#     1.URN是未来替代URL的趋势

# 二.提交数据方式
#   1.GET
#     1.标准GET没有请求体, 只能以查询字符串的形式提交数据
#   2.POST
#     1.查询字符串
#     2.请求体包含数据
#   Note:
#     1.查询字符串格式
#       1.?key=value
#       2.?key1=value1&key2=value2
#     2.网址有长度限制

# 三.HTTP无状态原因
#   1.短连接
#     1.TCP连接
#     2.基于HTTP传输数据 ~ 客户端请求, 服务端响应 ===> 通讯完成, 下次通讯重复1->2->3
#     3.TCP连接关闭
#   2.长连接


















