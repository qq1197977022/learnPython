# 一.三次握手
#   client                                                  server
#           客户端发送请求TCP连接 --->[1次] ~~> SYN
#             SEQUENCE NUMBER: 0
#             ACKNOWLEDGEMENT NUMBER: 0
#                                                     SYN+ACK <~~ [2次]<---服务端应答客户端请求
#                                                                            SEQUENCE NUMBER: 0
#                                                                            ACKNOWLEDGEMENT NUMBER: 1
#           1.客户端确认服务端应答 --->[3次] ~~> ACK
#               SEQUENCE NUMBER: 1
#               ACKNOWLEDGEMENT NUMBER: 1
#           2.紧随其后发送HTTP请求 --->           ~~~>       服务端先收到客户端TCP数据包, TCP连接建立成功, 随后收到客户端HTTP请求
#               SEQUENCE NUMBER: 1
#               ACKNOWLEDGEMENT NUMBER: 1
#                                                     <---1.确认
#                                                     <---2.响应HTTP请求
#                                                             SEQUENCE NUMBER: 1
#                                                             ACKNOWLEDGEMENT NUMBER: 101
# 二.四次挥手
#           1.确认收到收到HTTP响应数据包 ---->
#           2.客户端发送请求关闭TCP连接数据包 ---->[1次] ~~> FIN
#               SEQUENCE NUMBER: 101
#               ACKNOWLEDGEMENT NUMBER: 472
#                                                     ACK <~~ [2次]<---1.服务端发确认数据包
#                                                     FIN <~~ [3次]<---2.服务端发送关闭TCP连接数据包
#                                                                          SEQUENCE NUMBER: 472
#                                                                          ACKNOWLEDGEMENT NUMBER: 102
#           1.客户端确认服务端关闭TCP连接数据包---->[4次] ~~> ACK
#               SEQUENCE NUMBER: 102
#               ACKNOWLEDGEMENT NUMBER: 472
#









































