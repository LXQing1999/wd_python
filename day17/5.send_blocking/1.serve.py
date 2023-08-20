from socket import *
import select
import sys

tcp_server_socket = socket(AF_INET, SOCK_STREAM)

# 重用对应地址和端口
tcp_server_socket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
# 本地IP地址和端口
address = ('192.168.31.67', 2000)
tcp_server_socket.bind(address)
# 端口激活
tcp_server_socket.listen(100)
client_socket, clientAddr = tcp_server_socket.accept()
print(clientAddr)
# 服务器端accept之后，不去接缓冲区中的内容
while True:
    pass
