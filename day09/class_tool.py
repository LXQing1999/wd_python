"""
class_tool 
Author:LXQing
Date:2023/7/1
"""
class Tool(object):
    # 利用赋值语句,定义类属性,记录创建工具对象的总数
    count=0
    def __init__(self,name):
        self.name=name
        # 针对类属性做一个计数
        Tool.count+=1
    # 装饰器
# 给一个方法加上classmethod进行装饰,就是类方法
    @classmethod
    # cls拿到的是当前类名
    def show_tool_count(cls):
        print('工具对象的总数%d'%cls.count)
tool1=Tool('砧板')
tool2=Tool('剪刀')
tool3=Tool('菜刀')
print('创建了%d个工具'%Tool.count)
print('使用创建的菜刀对象也能访问类属性,创建了%d个工具'%tool3.count)
# 赋值的时候,新增了一个对象属性,这样写不规范
# 相当于创建了一个tool3.count
tool3.count=99
print('菜刀.工具属性.数量%d'%tool3.count)
print('创建了%d个工具'%Tool.count)