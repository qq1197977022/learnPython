#
# socket.listen([backlog])
#
#     Enable a server to accept connections.
#     If backlog is specified, it must be at least 0 (if it is lower, it is set to 0);
#         it specifies the number of unaccepted connections that the system will allow before refusing new connections.
#     If not specified, a default reasonable value is chosen.
#
#     Changed in version 3.5: The backlog parameter is now optional.


# 启动一个服务以接收connection
# 如果指定了参数backlog, 最小值为0(如果设置<0的值, 默认=0); 参数backlog设定在系统拒绝新的connection前, 允许的最大unaccepted连接数 ~ 未连接队列
# 如果没有指定, 将会自动设置一个合理的值

# Note
#   1.在linux下, 参数backlog是否设置都一样, 最大未连接数不限
#   2.MAC和Win下, 参数backlog设置有效

