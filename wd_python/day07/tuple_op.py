"""
tuple_op
元组的基本使用
Author:25423
Date:2023/6/27
"""
# 元组一个元素初始化要加逗号
test_tuple=(4,'lee','zhang','wang','lee')
print(type(test_tuple))

# 索引index 找到了第一个就直接返回了,不会输出两个结果
print(test_tuple.index('lee'))
# 统计计数
print(test_tuple.count('lee'))
print(len(test_tuple))
print("总人数%d  姓氏%s %s %s %s"%test_tuple)

test2=tuple(i for i in range(10))
print(test2)