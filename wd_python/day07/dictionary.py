"""
dictionary 字典
是无序对象的集合 有点像结构体
Author:25423
Date:2023/6/27
"""
stu={"num":123, "name": "lee", "gender":"male"}
print(stu)
stu["num"]=456 # 重新赋值
# 增
stu.setdefault('score',90)  # 添加值
print(stu)
stu.update({'name': "wang"})  # 更新值
print(stu)
# 删除
del stu['gender']
print(stu)

# 查
# print(stu['math'])   # 找不到会直接报错
# 只能通过键查值 通过值来查找键,需要遍历
# get找不到会返回 None 健壮性更好 代码不容易崩溃
print(stu.get('math'))
print('item键值对')
for i in stu.items():
    print(i)
print('键')
for i in stu.keys():
    print(i)
print('值')
for i in stu.values():
    print(i)

# print("找不到就返回None",stu.fromkeys({"rank": 1}))

# 清空
stu.clear()
print('空字典',stu)