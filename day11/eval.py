"""
eval
将字符串当成有效的表达式来求值,并返回计算结果
可以用来读配置文件
Author:LXQing
Date:2023/7/4
"""
print('将字符串"string" 变成数值',eval("1+1"))
print('将字符串"string" 变成字典',eval("{'name':'lee','age':18}"))
print('将字符串"string" 变成列表',eval("[1,2,3,4,5]"))

# 安全风险,不要用eval执行前端传来的字符串,会执行删除操作
eval("__import__('os').remove('file_del.txt')")
