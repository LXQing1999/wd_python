"""
list_generator
列表生成式 :快速的生成列表
代码短,但可读性差
Author:25423
Date:2023/6/26
"""
a = [i for i in range(10)]
print(a)
b = []
for i in range(10):
    b.append(i)
print(b)

# 双重for循环  右边的for循环在里面
a = [j for i in range(10) for j in range(3)]
print(a)
a = [[i * j for i in range(10)] for j in range(3)]
print(a)
# 这个x在这里应该是a中每一行
# j是每一个x小组中的单个元素
a = [j for x in a for j in x]
print('二维数组转一维数组：', a)
