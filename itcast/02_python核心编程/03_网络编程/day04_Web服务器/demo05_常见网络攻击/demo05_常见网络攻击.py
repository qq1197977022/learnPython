# 1.TCP半连接攻击
#   1.又称SYN Flood(SYN洪水), 典型的DoS(Denial of Service 拒绝服务)攻击
#   2.耗尽服务器TCP连接资源, 停止响应正常TCP连接请求

# 2.DNS攻击
#   1.攻陷DNS服务器, 解析假ip
#     eg. 把域名解析为钓鱼网站服务器ip

# 3.DNS欺骗
#   1.不断给当前网段所有主机发送DNS应答数据包, 即使收到真实DNS服务器应答数据包, 随后也会因收到假DNS应答数据包, 更新域名对应的真实IP到假的DNS应答数据包该域名对应的IP

# 4.ARP攻击


# Note
#   1.上述攻击必须使用原始套接字

#   2.查看域名解析IP
#     1.nslookup 域名
#     eg.
#         C:\Users\kc>nslookup baidu.com
#         服务器:  dnspai-public-dns.dnspai.com
#         Address:  101.226.4.6
#
#         非权威应答:
#         名称:    baidu.com
#         Addresses:  111.13.101.208
#                   220.181.57.216






