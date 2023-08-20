from socket import *
import sys
import select

tcp_client_socket = socket(AF_INET, SOCK_STREAM)
address = ('192.168.31.67', 2000)

tcp_client_socket.connect(address)
temp_str='a'*1000
total=0
try:
    while True:
        # MSG_DONTWAIT
        send_size=tcp_client_socket.send(temp_str.encode('utf8'),MSG_DONTWAIT)
        total+=send_size
        print(total)
        if send_size!=1000:
            print("peer close")
            exit(1)
except Exception as e:
    print(e)
