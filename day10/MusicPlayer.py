"""
MusicPlayer 
Author:LXQing
Date:2023/7/1
"""
class MusicPlayer(object):
    instance=None
    @classmethod
    def __new__(cls, *args, **kwargs):
        if cls.instance is None:
        # 创建对象时,new方法会被自动调用
            print('创建对象,分配空间')
        # 分配地址空间
            cls.instance=super().__new__(cls)
        # 返回对象的引用
        # "%x"将其以十六进制形式输出
        # print('%x'%id(instance))
        return cls.instance
    def __init__(self):
        print('初始化')
player1=MusicPlayer('Lana')
player2=MusicPlayer('Chow')
print(player1)
print(player2)
