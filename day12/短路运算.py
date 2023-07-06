"""
短路运算 
Author:LXQing
Date:2023/7/6
"""
# 1==1 and print('hello')
# 1==0 and print('hello')
# range(起始,运算,判断) 从4开始，每次递减1,递减到-1(开区间,所以不包含)，
for i in range(10//2-1,-1,-1):
    print(i)
