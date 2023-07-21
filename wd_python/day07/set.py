"""
set 
Author:25423
Date:2023/6/27
"""
dict1={}
print(type(dict1))

# 定义空集合
set1=set()
fruits={'apple','banana'}
company={'apple','ibm','GE'}
print('不同之处',fruits.difference(company))
print('联合',fruits.union(company))
x={'a','b','c'}
y={'b','c'}
print(y.issubset(x))
print('删除',company.discard('ibm'))
# set里面的元素是不重复的
print(set('ababsdbwa'))
