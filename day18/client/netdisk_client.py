"""
netdisk_client
Author:LXQing
Date:2023/08/22
"""
from socket import *
import struct


class Client:
    def __init__(self, ip, port):
        self.client:socket = None
        self.ip = ip
        self.port = port

    def tcp_connect(self):
        self.client = socket(AF_INET, SOCK_STREAM)
        self.client.connect((self.ip, self.port))

    def send_train(self, send_bytes):
        train_head_bytes = struct.pack('I', len(send_bytes))
        self.client.send(train_head_bytes + send_bytes)

    def recv_train(self):
        '''
        recv火车，就是把火车接收的内容返回回去
        :return:
        '''
        train_head_bytes = self.client.recv(4)
        train_head = struct.unpack('I', train_head_bytes)
        return self.client.recv(train_head[0])

    def send_command(self):
        while True:
            command = input()
            self.send_train(command.encode('utf8'))
            if command[:2] == 'ls':
                self.do_ls()
            elif command[:2] == 'cd':
                self.do_cd(command)
            elif command[:3] == 'pwd':
                self.do_pwd()
            elif command[:2] == 'rm':
                self.do_rm(command)
            elif command[:4] == 'gets':
                self.do_gets(command)
            elif command[:4] == 'puts':
                self.do_puts(command)
            else:
                print('Wrong command')

    def do_ls(self):
        data=self.recv_train().decode('utf8')
        print(data)
    def do_cd(self):
        print(self.recv_train().decode('utf8'))

    def do_pwd(self):
        print(self.recv_train().decode('utf8'))

    def do_rm(self):
        pass


if __name__ == '__main__':
    client = Client('192.168.31.67', 2000)
    client.tcp_connect()
    client.send_command()
