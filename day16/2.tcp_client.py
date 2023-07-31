"""
2.tcp_client客户端

socket.socket() - 这是一个用于创建套接字对象的函数。
socket.AF_INET6 - 这个参数指定了套接字的地址族，用于支持IPv6地址。
socket.SOCK_STREAM - 这个参数指定了套接字的类型，用于支持TCP协议。
socket.socket(socket.AF_INET, socket.SOCK_STREAM)  是创建一个支持IPv6地址和TCP协议的套接字对象。

Author:LXQing
Date:2023/07/29
"""
import socket


def tcp_client():
    # ip地址和字节流
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destation_addr = ('192.168.31.67', 2000)
    # tcp连接三次握手
    client.connect(destation_addr)
    # 先接
    byte_stream=client.recv(100)
    print(byte_stream.decode('utf8'))
    client.send('tcp_client客户端'.encode('utf8'))
    client.close()


if __name__ == '__main__':
    tcp_client()
