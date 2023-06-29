"""
Parameter 可变参数 不可变参数
Author:LXQing
Date:2023/6/28
"""
def change(num_list):
    # 在list后面添加新元素
    num_list.extend([1,2,3])
    print(num_list)
original_list=[4,5,6]
print(change(original_list))
