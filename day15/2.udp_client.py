"""
2.udp——client客户端
Author:LXQing
Date:2023/07/26
"""
import socket
client=socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
destation_addr=('192.168.31.67',2000)
# b'hello'强制转换成二进制
# client.sendto(b'hello',destation_addr)
# 注意编码形式
# client.sendto('리수칭你好こんにちはhello'.encode('utf8'),destation_addr)
client.sendto('HELLO'.encode('utf8'),destation_addr)
data,_=client.recvfrom(100)
print(data.decode('utf8'))
client.close()