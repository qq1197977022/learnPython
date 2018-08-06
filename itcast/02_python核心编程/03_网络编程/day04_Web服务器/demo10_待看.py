import socket
import queue
import select


def main():
    server = socket.socket(family=socket.AF_INET, type=socket.SOCK_STREAM)
    server.setblocking(False)   # 非阻塞
    serve_ip_port = ('', 8080)
    server.bind(serve_ip_port)
    server.listen(5)

    message_queue = {}
    rlist = [server]
    wlist = []
    xlist = []
    while True:
        readable, writeable, xable = select.select(rlist, wlist, xlist)
        for sock_obj in readable:
            if sock_obj == server:
                rs_sock, client_ip_port = server.accept()
                rlist.append(rs_sock)
                print(f'客户端{client_ip_port}已连接')

                message_queue[rs_sock] = queue.Queue()
            else:
                try:
                    recv_bytes = sock_obj.recv(1024)
                    if len(recv_bytes) == 0:
                        sock_obj.close()
                        print(f'客户端{client_ip_port}已关闭连接')
                        break
                    else:
                        data = recv_bytes.decode('GBK')
                        print(f'\t客户端: {client_ip_port[1]}: {data}')
                        message_queue[sock_obj].put(data)
                        if sock_obj not in wlist:
                            wlist.append(sock_obj)
                except ConnectionResetError:
                    rlist.remove(sock_obj)
                    del message_queue[sock_obj]
                    print(f'{client_ip_port}已关闭连接')

        for rs_sock in wlist:
            try:
                if not message_queue[rs_sock].empty():
                    send_data = message_queue[rs_sock].get()
                    rs_sock.send(send_data.encode('GBK'))
                else:
                    wlist.remove(rs_sock)
            except ConnectionResetError:
                del message_queue[rs_sock]
                wlist.remove(rs_sock)
                print(f'客户端{client_ip_port}断开连接')


if __name__ == '__main__':
    main()

























