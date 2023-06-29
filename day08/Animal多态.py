"""
poly多态
同一种操作可以作用于不同的对象，并且可以根据对象的类型自动选择适当的方法进行执行。
提高代码的灵活性和可复用性。
Author:LXQing
Date:2023/6/29
"""
class Animal:
    # 方法
    def make_sound(self):
        pass

# 衍生出两个子类
class Dog(Animal):
    def make_sound(self):
        print("汪汪汪")


class Cat(Animal):
    def make_sound(self):
        print("喵喵喵")

'''定义一个函数make_animal_sound函数接受一个Animal类型的参数animal，
然后调用animal的make_sound方法。
当我们将一个Dog对象传入该函数时，会调用Dog类中的make_sound方法
同一个操作make_sound应用于不同的对象，得到了不同的结果。'''
def make_animal_sound(animal):
    animal.make_sound()


animal1 = Dog()
animal2 = Cat()

make_animal_sound(animal1)
make_animal_sound(animal2)
