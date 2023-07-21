"""
multiple_inheritance 多重继承
Author:LXQing
Date:2023/6/29
"""
class A:
    def demo(self):
        print('A demo')
        pass
    def test(self):
        print('A test')


class B:
    def demo(self):
        print('B demo')
    def test(self):
        print('B test')
class C(A,B):
    def demo(self):
        print('C demo')
    pass
print('按顺序列出继承关系,对应哪个方法',C.__mro__)
c=C()
c.demo()
