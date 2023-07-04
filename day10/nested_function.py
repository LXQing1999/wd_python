"""
nested_function
异常的传递 -嵌套函数
Author:LXQing
Date:2023/7/2
"""
def demo1():
    num=int(input("输入整数: "))
    print('数据类型不对')
    return num
def demo2():
    return demo1()

# 利用异常的传递性,在主程序捕捉异常
try:
    print(demo2())
except Exception as e:
    print('发生异常 %s'%e)
finally:
    # 异常时候,第8行直接抛到Exception,不会return num
    # 所以finally打印不出num
    print('end')
