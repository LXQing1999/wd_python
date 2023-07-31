"""
file_client
Author:LXQing
Date:2023/07/29
"""
from socket import *


def main():
    # 创建 socket
    tcp_client_socket = socket(AF_INET, SOCK_STREAM)
    # 目的信息
    server_ip = '192.168.31.67'
    # 服务器端口 端口2000默认是sccp协议
    server_port = 2000
    # connect()函数用于建立与服务器的连接，它的参数应该是一个元组，包含服务器的IP地址和端口号。
    tcp_client_socket.connect((server_ip,server_port))
    # 输入需要下载的文件名
    file_name = input("请输入要下载的文件名：")
    # 发送文件下载请求
    tcp_client_socket.send(file_name.encode("utf-8"))
    # 接收对方发送过来的数据，最大接收 1024 个字节（1K）
    recv_data = tcp_client_socket.recv(1024)
    # print('接收到的数据为:', recv_data.decode('utf-8'))
    # 如果接收到数据再创建文件，否则不创建
    if recv_data:
        with open("[接收]" + file_name, "wb") as f:
            f.write(recv_data)
    # 关闭套接字
    tcp_client_socket.close()


if __name__ == "__main__":
    main()
