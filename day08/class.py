"""
class 类 对象
1.在内存中申请空间 new
2.为各属性申请初始值init

Author:LXQing
Date:2023/6/28
"""
class Person():
    def __init__(self,name,age,height):
        self.name=name
        self.age=age
        self.height=height
    def run(self):
        print("%s"%self.name)
    def year(self):
        print('%s'%self.age)
    def high(self):
        print('%s' % self.height)

#
lee=Person('lee',18,180)
lee.run()
lee.year()
lee.high()
wong=Person('wong',19,165)
wong.run()
wong.year()
wong.high()
zhang=lee
print('相当于把lee的内容,都赋给了zhang')
zhang.run()
