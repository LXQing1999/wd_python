"""
sorted
pycharm中竖直选中shift+alt+鼠标左键
Author:LXQing
Date:2023/7/8
"""
from operator import itemgetter


def sort_str():
    l = 'This is a test string'.split()
    print(l)
    # key对应一个函数，注意不要加（）
    # 加了括号返回一个结果，就不对了
    print(sorted(l, key=str.lower))


def my_func(i):
    return i[1]


def sort_list_tuple():
    stu_tuples = [('ann', 'D', 66), ('bob', 'B', 77), ('zhang', 'C', 88)]
    # lambda匿名函数  sorted默认是升序
    # key是传入了自定义的函数
    print(sorted(stu_tuples, key=lambda k: k[2], reverse=True))
    print(':前的名字可以自定义', sorted(stu_tuples, key=lambda i: i[2], reverse=True))
    print(sorted(stu_tuples, key=my_func))


class Stu:
    def __init__(self, name, grade, score):
        self.name = name
        self.grade = grade
        self.score = score

    # 实现类到字符串的转化,里面可以放一个元组类型
    def __repr__(self):
        return repr((self.name, self.grade, self.score))


def dict_list():
    mydict = {'lee': ['M', 5], 'zhang': ['E', 6], 'wang': ['P', 3]}
    # item 是将键和值以元组的形式组合在一起
    print(sorted(mydict.items(), key=lambda i: i[0][0]))


def use_stablility():
    l = [('red', 3), ('blue', 1), ('green', 4), ('blue', 2)]
    l.sort(key=itemgetter(0))
    print(l)


'''排序的列表里是自定义的object
lambda函数是一个匿名函数，可以在一行代码中定义。
它的语法形式为：lambda 参数列表: 表达式。
lambda函数的参数s代表了stu列表中的每个学生对象，
表达式s.name返回了每个学生对象的name属性的值。
这个s是可以自定义的，换成i也可以
'''


def sort_list_object():
    stu = [Stu('ann', 'D', 66), Stu('bob', 'B', 77), Stu('zhang', 'C', 88)]
    sorted(stu, key=lambda s: s.name)
    print(stu)


# 列表中含有字典
def list_dist():
    gamelist = [{"name": "Bob", "wins": 10, "losses": 3, "rating": 75.00},
                {"name": "David", "wins": 3, "losses": 5, "rating": 57.00},
                {"name": "Carol", "wins": 4, "losses": 5, "rating": 57.00},
                {"name": "Patty", "wins": 9, "losses": 3, "rating": 71.48}]
    print(sorted(gamelist, key=itemgetter('rating')))


if __name__ == '__main__':
    sort_list_object()
    use_stablility()
    dict_list()
    list_dist()
