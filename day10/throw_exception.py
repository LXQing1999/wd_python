"""
throw_exception 抛出异常
Author:LXQing
Date:2023/7/2
"""
def input_passwoed():
    password=input('请输入密码: ')
    if len(password)>=8:
        return password
    # 如果密码长度＜8主动抛出异常
    print('主动抛出异常')
    # 创建异常对象-可以使用错误信息字符作为参数
    ex=Exception('密码长度不够')
    # 主动抛出异常  raise关键字用于引发异常。它允许程序员手动引发异常，而不是等待发生错误时自动引发异常。
    # raise关键字用于引发异常。它允许程序员手动引发异常，而不是等待发生错误时自动引发异常。
    raise ex
    print('透明transparency')

# 提示用户输密码
try:
    print(input_passwoed())
except Exception as e:
    print(e)
