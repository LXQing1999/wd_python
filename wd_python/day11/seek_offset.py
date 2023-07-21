"""
seek_offset
在查找汉字时,偏移量需要是3的倍数,否则会报错  invalid start byte
偏移量offset就是指针的偏移位置,从此处开始
Author:LXQing
Date:2023/7/4
"""
def use_seek():
    file=open('file',mode='r+',encoding='utf8')
    file.seek(3)
    text=file.read()
    print(text)
    file.close()

# 字节流 这个以字节为基本单位,所以offset填几都行
# 在字节流,读入的时候,必须强制转换成b' '同样格式的才能写进去
def write_binary():
    file = open('file', mode='rb+')
    file.seek(1)
    text1 = file.read()
    print(text1)
    text2=file.write(b'LXQing')
    # 指定格式保存
    text2 = file.write('分子医学'.encode('utf8'))
    print(text2)
    file.close()


if __name__ == '__main__':
    # use_seek()
    write_binary()