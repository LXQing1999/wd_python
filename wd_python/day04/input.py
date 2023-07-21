"""
input
强制类型转换
Author:25423
Date:2023/6/25
"""
# 默认输入的是string类型的
x = input('请输入:')
print(type(x))
print(int(x) / 2)
print(float(x) / 2)

name = 'Ann'
stu_num = 123
height = 1.63
print("名字:%s" % name)
# 用0补全六位数字
print("学号:%06d" % stu_num)
# 浮点数 保留两位小数
print("身高:%.02f" % height)
print("名字%s 学号:%06d 身高:%.02f米" % (name, stu_num, height))
