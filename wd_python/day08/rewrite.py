"""
rewrite 重写
在不改变父类的情况下重写代码
Author:LXQing
Date:2023/6/29
"""
class Dog:
    def bark(self):
        print('汪汪')
class SkyDog(Dog):
    def bark(self):
# 使用super调用原本在父类Dog中封装的方法
        super().bark()
        print('嗷呜汪汪汪汪汪汪')

xiaotian=SkyDog()
xiaotian.bark()

