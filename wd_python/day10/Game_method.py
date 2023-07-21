"""
Game_class
@staticmethod是一个装饰器，用于定义静态方法。
静态方法是指    与类相关联  但 不需要访问类实例或类属性的方法。
静态方法不需要通过实例化类来调用，可以直接通过类名调用。
静态方法不能访问类的属性，也不能访问实例的属性。

@classmethod装饰器用于定义一个接受类作为第一个参数的方法。
将方法绑定到类，而不是实例上。这意味着类方法可以被类本身调用，而不需要创建实例。
Author:LXQing
Date:2023/7/1
"""
class Game(object):
    top_score=0  # 记录历史最高分
    def __init__(self,player_name):
        self.player_name=player_name
    @staticmethod
    def show_help():
        print('游戏加载中...')
    @classmethod
    def show_top_score(cls):
        print('历史最高记录%d'%cls.top_score)
    def start_game(self):
        print('%s游戏开始啦~'%self.player_name)

Game.show_help()
Game.show_top_score()
game=Game('张三')
game.start_game()