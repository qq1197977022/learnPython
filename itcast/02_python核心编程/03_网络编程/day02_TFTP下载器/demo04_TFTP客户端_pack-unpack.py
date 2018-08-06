import socket
import struct
# 该模块执行Python值和用Python字节对象表示的C结构体之间转换
#   1.处理存储在文件, 网络链接, 其他资源中的二进制数据
#   2.使用指定的格式化字符串作为C结构体和Python值的预期转换的布局的紧凑描述


def main():
    udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # 创建UDP socket对象
    pack_data = struct.pack('!h10sb5sb', 1, b'demo04.txt', 0, b'octet', 0)    # TFTP下载请求协议, 网络大端

    dst_addr_port = ('192.168.85.1', 69)  # destination
    udp_socket.sendto(pack_data, dst_addr_port)  # 发

    recv_data = udp_socket.recvfrom(1024)  # 收
    recv_data_bytes = recv_data[0]  # 服务端发送字节数据
    recv_data_addr = recv_data[1]   # 服务端发送数据包IP + 随机port

    option_block_code = struct.unpack('!hh', recv_data_bytes[:4])  # 2个字节表示操作码, 2个字节表示块编号
    option_code = option_block_code[0]   # 操作码
    block_code = option_block_code[1]    # 块编号

    if option_code != 5:
        file = open('demo04.txt', 'wb')
        file.write(recv_data_bytes[4:])

        while len(recv_data_bytes) >= 516:
            ack = struct.pack('!hh', 4, block_code)    # 确认反馈数据包
            udp_socket.sendto(ack, recv_data_addr)

            recv_data_bytes = udp_socket.recv(1024)
            block_code = struct.unpack('!hh', recv_data_bytes[:4])[1]
            file.write(recv_data_bytes[4:])
        file.close()
    else:
        print('出错...')

    udp_socket.close()


if __name__ == '__main__':
    main()


# 问题
# 1.为什么不写入文件, 直接解码输出报错?
#   data = recv_data_bytes[4:].decode('UTF-8')
#   print(data)
# 2.为什么在While循环中设置延时, 下载数据有错?


# 一.内存地址从0X000...开始编号, 低位到高位
#   1.小端: 高低位对应存储
#   2.大端: 高低位相反存储
#     eg.
#       1.个人PC: 小端
#       2.IBM等大型服务器: 大端
#   3.网络协议规定以大端为准






