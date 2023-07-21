"""
file_op.txt 文件操作
编码格式为utf-8
注意open打开的地址是 相对路径
如果不写的话,默认是当前文件夹的文件

r只读 w只写(会覆盖原文)
r+会把新内容放在开头,w+会覆盖原有内容,
a+文件已存在会放在结尾,不存在会创建新文件
Author:LXQing
Date:2023/7/3
"""

def txt_open():
    file = open('file_op.txt', encoding='utf-8')
    # 读取 ()里可以填写读取几个字符
    # 读到文件字符结尾会看到空字符串
    text = file.read()
    print(text)
    # text=file.read(9)
    # print(text)
    # 关闭
    file.close()


def txt_write():
    file = open('file_op.txt', mode='r+', encoding='utf-8')
    file.write('****write*****')
    file.close()


def txt_readline():
    file = open('file_op.txt', mode='r+', encoding='utf-8')
    while True:
        text = file.readline()
        # 文件读结束了
        if not text:
            break
        print(text, end=' ')
    file.close()


# 文件指针定位方法
def txt_seek():
    file = open('file_op.txt', mode='r+', encoding='utf-8')
    # 写入
    file.write('****write*****')
    file.seek(2)
    text = file.read()
    print('偏移了几个指针',text)
    file.close()

def open_binary():
    file = open('file_op.txt', mode='rb+')
    # 二进制模式下的字节流  计网中的物理层
    text=file.read()
    file.close()

if __name__ == '__main__':
    # txt_open()
    # txt_write()
    # txt_readline()
    # txt_seek()
    open_binary()
