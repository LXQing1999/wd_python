"""
operator2 
Author:25423
Date:2023/6/25
"""
# 赋值运算符
def assign():
    a=3
    a+=4
    print(a)
    b=4
    b*=a
    print(b)
# 位运算
def bit():
    i=5
    j=7
    # 按位  与
    print(i&j)
    # 按位  或
    print(i | j)
    # 按位取反
    print(~i)
    # 异或
    print(i ^j)
    # 左移一位相当于×2
    print(i<<1)
    # 右移一位相当于整除2 没有小数部分
    print(i>>1)
    i,j=j,i
    print(i,j)
if __name__ == '__main__':
    assign()
    bit()