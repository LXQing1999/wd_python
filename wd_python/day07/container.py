"""
container 容器
Author:25423
Date:2023/6/27
"""
a=[1,2]
b=[3,4]
print('list合并',a+b)

x={'name':'lee'}
y={'age':18}
print('name' in x)

# 初始化
a=[0]*10
print(a)
a[3]=3
print(a)
print('是否在字符串内','a' in 'abc')

print('元组比大小,只比首字母就返回',(1,2,3)<(2,5,-2))