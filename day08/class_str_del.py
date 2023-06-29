"""
str_del 
Author:LXQing
Date:2023/6/28
"""
class Cat:
    # 申请一个新空间
    def __init__(self,new_name):
        self.name=new_name
        print("%s"%self.name)
    # 对象销毁的时候调用
    def __del__(self):
        print("去除%s"%self.name)
    # 如果不重写,返回的是一个地址
    # 必须返回一个字符串,打印对象
    def __str__(self):
        return "猫咪[%s]"%self.name

tom=Cat('Tom')
print(tom)
# del tom




