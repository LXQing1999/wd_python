"""
file_server
需要右键，在运行设置的参数中将端口改为2000才能正常运行
Author:LXQing
Date:2023/07/29
"""
from socket import *
import sys


# 获取文件内容
def get_file_content(file_name):
    try:
        # 以二进制的形式打开
        with open(file_name, "rb") as f:
            content = f.read()
        return content
    except:
        print("没有下载的文件：%s" % file_name)


def main():
    # 没传参的时候为1
    if len(sys.argv) != 2:
        print("请按照如下方式运行：python3 xxx.py 2000")
        return
    else:
        # 运行方式python3 xxx.py 7890
        port = int(sys.argv[1])
    # 创建socket数据
    tcp_server_socket = socket(AF_INET, SOCK_STREAM)
    # 本地信息
    address = ('', port)
    # 绑定本地信息
    tcp_server_socket.bind(address)
    # 将主动套接字变为被动套接字
    tcp_server_socket.listen(128)

    while True:
        # 等待客户端的连接，为这个客户端发送文件
        client_socket, clientAddr = tcp_server_socket.accept()
        # 接收对方发送来的数据
        recv_data = client_socket.recv(1024)
        file_name = recv_data.decode("utf8")
        print("对方请求下载的文件名：%s" % file_name)
        file_content = get_file_content(file_name)
        # 发送文件的数据给客户端获取打开文件时是以rb方式打开，所以已经是二进制格式，不用重新encode了
        if file_content:
            client_socket.send(file_content)
        # 关闭这个套接字
        client_socket.close()
        # 关闭监听套接字
        tcp_server_socket.close()


if __name__ == "__main__":
    main()
