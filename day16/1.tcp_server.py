"""
1.tcp_server服务器
一定要先启动run服务器，因为服务器要等待
tcp连接保证传输的正确，缓冲区充满了可能会阻塞
udp连接直接传给路由器，多了直接被丢弃
Author:LXQing
Date:2023/07/29
"""
import socket

# 定义tcp服务器
def tcp_server():
    # tcp的缓冲区
    s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    addr=('192.168.31.67',2000)
    # 绑定,端口并没有激活
    s.bind(addr)
    # listen时，端口才激活
    s.listen(128)
    print('连接和监听的过程对程序员来说是透明的')
    new_client,client_addr=s.accept()
    print(client_addr)
    # send recv操作  把recv放在前面容易阻塞
    new_client.send('tcp_server服务器发出'.encode('utf8'))
    byte_stream=new_client.recv(100)
    print(byte_stream.decode('utf8'))
    new_client.close()# 和客户端断开连接
    s.close() # 关闭监听
if __name__=='__main__':
    tcp_server()