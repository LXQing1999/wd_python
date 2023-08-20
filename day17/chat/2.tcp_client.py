"""
2.tcp_client客户端
现在写的这个是只能发送一条消息的

Author:LXQing
Date:2023/08/11
"""
import socket


def tcp_client():
    # ip地址和字节流
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    destation_addr = ('192.168.31.67', 2000)
    # tcp连接三次握手
    client.connect(destation_addr)

    while True:
        data=input()
        # 发送给服务器端
        client.send(data.encode('utf8'))
        # 接收服务器传回的信息
        data=client.recv(1000)
        print(data.decode('utf8'))
    client.close()


if __name__ == '__main__':
    tcp_client()
