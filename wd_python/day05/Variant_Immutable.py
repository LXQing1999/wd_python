"""
Variant_Immutable 
Author:25423
Date:2023/6/26
"""
# 可变数据类型 同一个地址下面存了不一样的数据
def demo_list():
    demo_list = [1, 2, 3]
    print(list, type(demo_list))
    print('列表地址:%d' % id(demo_list))
    demo_list[0] = 9
    for i in range(3):
        print(demo_list[i], end=' ')
    print('新列表地址:%d' % id(demo_list))


# 可变数据类型可以在子函数中通过接口修改数据空间中的值
def change(my_list):
    my_list[0] = 20


def address_tuple():
    tuple1 = (1, 2, 3)
    tuple2 = (1, 2, 3)
    print('同样内容的元组地址')
    print(id(tuple1))
    print(id(tuple2))


# 不可变数据类型只能用等号通过赋值运算符直接赋值
def demo_tuple():
    test_tuple = (1, 2, 3)
    print(id(test_tuple))
    # print(test_tuple[0])
    test_tuple = (4, 5, 6)
    print(id(test_tuple))


if __name__ == '__main__':
    list_test = [1, 2, 3]
    change(list_test)
    print(list_test)
    demo_tuple()
    address_tuple()
