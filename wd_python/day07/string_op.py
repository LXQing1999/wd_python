"""
string 
Author:25423
Date:2023/6/27
"""
# import string
str1=' '
print(str1.isspace())
str2='hello'
print(str2.isalpha())
print(str2.replace('h','H'))
print(str2.upper())
print('调换大小写',str.swapcase(str2.replace('h','H')))
str3=' 123 '
str4=' add '
str_uni=str3+str4
print(str_uni)
print('以分隔符拆分',str_uni.split())
print('拆分成三部分',str_uni.partition(str_uni))
print('去掉左右两边的空白字符',str_uni.strip())
list1=['a','b','c']
str_join='-'
print('列表变字符串 连接组合',str_join.join(list1))
print('换行',str_uni.splitlines())
# print(str3.isdigit())
# print(str3.decimal())
