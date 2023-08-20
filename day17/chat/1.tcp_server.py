"""
1.tcp_server服务器
只能轮流发消息
Author:LXQing
Date:2023/08/11
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
    while True:
        # 服务器端先接
        data=new_client.recv(100)
        print(data.decode('utf8'))
        data=input() # 服务器端说话，发给用户端
        new_client.send(data.encode('utf8'))




    new_client.close()# 和客户端断开连接
    s.close() # 关闭监听
if __name__=='__main__':
    tcp_server()