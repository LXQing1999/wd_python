"""
mult_fun多值函数 可变参数
Author:LXQing
Date:2023/6/28
"""
'''num只能存下一个数 
*agrs是一个指针,指向一个地址,可以随意装数据,事实上是一个元组
**kwargs是一个字典的起始地址,代表键值对'''
def mult_fun(num,*agrs,**kwargs):
    print(num,agrs,kwargs)
    print('将agrs,kwargs作为了整体的参数,agrs,kwargs都成了元组的一部分元素,而字典是空的')
    mult_fun2(agrs,kwargs)
    print('但是agrs,kwargs加上指针后,指向的是地址,引用时仍作为元组和字典,能够正确输出')
    mult_fun2(*agrs, **kwargs)

def mult_fun2(*agrs,**kwargs):
    print(agrs,kwargs)
if __name__ == '__main__':
    mult_fun(1, 2, 3, 4, 5, name='lee', age=18, gender=True)



