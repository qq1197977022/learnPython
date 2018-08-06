import socket
import time
udp_socket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
udp_socket.bind(('192.168.102.2', 8080))
while True:
    data = udp_socket.recv(1024)
    print(data.decode('GBK'))
    time.sleep(0.1)



