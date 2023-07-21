"""
Private_properties__methods
私有属性和私有方法
私有属性只能被类自己的方法调用
Author:LXQing
Date:2023/6/29
"""
# 类的名字要大写
class Stu:
    def __init__(self, name):
        self.name = name
        # __开头的这个叫私有属性
        # 在外部打印时会报错
        self.__score = 65
    def secret(self):
        print("成绩是%d" % self.__score)
    '''一般不写这种_的
    def _salary(self):
        self._salary=10000'''

lee = Stu('李')
# 私有属性,外部直接访问会报错
# print("成绩是%d"%self.__score)
# 除非调用,这是为了防止每次调用的时候修改数据出错
lee.secret()
# print(lee._salary())

