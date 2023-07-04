"""
static_method 静态方法
Author:LXQing
Date:2023/7/1
"""
class Dog():
    @staticmethod
# 方法内,不需要访问实例属性和类属性
    def run():
        print('run run run')
Dog.run()