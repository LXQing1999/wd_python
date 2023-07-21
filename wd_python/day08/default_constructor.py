"""
default_constructor 缺省函数
Author:LXQing
Date:2023/6/28
"""
def info(name,gender=True):
    # 不传进去默认是female
    # 注意Python里不能像c++一样写!
    if not gender:
        gender='male'
    else:
        gender = 'female'
    print("%s %s"%(name,gender))

if __name__ == '__main__':
    info('lee',)
    info('lee', False)
    info('lee', True)