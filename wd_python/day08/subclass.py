"""
subclass
子类中去使用父类的私有属性和私有方法
Author:LXQing
Date:2023/6/29
"""
class A:
    def __init__(self):
        self.num1=100
        # __私有属性
        self.__num2=200
    def __test(self):
        print('私有方法 %d %d'%(self.num1,self.__num2))
'''1.在子类的对象方法中,不能访问父类的私有属性self.__num2
2.在子类的对象方法中,不能调用父类的私有方法 __test'''
class B(A):
    def demo(self):
        # self.__test()   不能调用父类的私有方法
        pass
b=B()
b.demo()