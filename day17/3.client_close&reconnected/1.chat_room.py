"""
1.tcp_server服务器
真正的即时聊天
Author:LXQing
Date:2023/08/11
"""
import socket
import select
import sys


# 定义tcp服务器
def tcp_server():
    '''
    socket 是 Python 中的一个模块，提供了用于网络编程的功能。         socket.AF_INET 是一个常量，表示使用IPv4协议。
    socket.SOCK_STREAM 也是一个常量，表示使用TCP协议。
    socket.socket(socket.AF_INET, socket.SOCK_STREAM) 是一个函数调用，创建了一个套接字对象，该对象使用了IPv4协议和TCP协议。
    这个套接字对象可以用于建立客户端或服务器端的网络连接，通过调用套接字对象的方法，可以进行网络数据的发送和接收操作。'''
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    addr = ('192.168.31.67', 2000)
    # 绑定,端口并没有激活
    s.bind(addr)
    # listen时，端口才激活
    s.listen(128)
    new_client, client_addr = s.accept()
    print(client_addr)
    # 创建一个epoll对象
    # fileno文件描述符
    # select.EPOLLIN 可读事件
    epoll = select.epoll()
    # 让epoll监控new_client sys.stdin
    epoll.register(new_client.fileno(), select.EPOLLIN)
    epoll.register(sys.stdin.fileno(), select.EPOLLIN)
    client_list = []
    print(new_client.fileno())
    # epoll.register()
    print(sys.stdin.fileno())
    # fds数组就是需要监听的文件描述符数组
    while True:
        # epoll.poll(-1)是一个阻塞调用，它会等待直到有事件发生才返回。它的功能是监视文件描述符上的事件，并返回就绪的文件描述符列表。
        events = epoll.poll(-1)
        for fd, event in events:
            # fileno() 方法返回一个整型的文件描述符(file descriptor FD 整型)
            if fd == s.fileno():
                # 有客户端连接，就连上，注册
                new_client, client_addr = s.accept()
                print(client_addr)
                client_list.append(new_client)
                epoll.register(new_client.fileno(), select.EPOLLIN)
            #  recv、select和epoll都是阻塞方法   如果接收缓冲区有数据
            else:
                remove_client = None
                for client in client_list:
                    if client.fileno() == fd:
                        data = client.recv(100)
                        if data:
                            # print(data.decode('utf8'))
                            for other_client in client_list:
                                if other_client is client:  # 不发给自己
                                    pass
                                else:
                                    other_client.send(data)
                        else:  # 断开了就记录一下
                            remove_client=client
                if remove_client==True:
                    client_list.remove(remove_client)
                    epoll.unregister(remove_client.fileno())
                    remove_client.close()

    s.close()  # 关闭监听


if __name__ == '__main__':
    tcp_server()
