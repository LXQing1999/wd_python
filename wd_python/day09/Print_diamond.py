"""
Print_diamond 
Author:LXQing
Date:2023/6/30
"""
# print('hello')
i=1
while i<=9:
    j = 1
    # 打印空格
    while j<=abs(5-i):
        print(' ',end='')
        j+=1
    j=1
    while j<=9-2*abs(5-i):
        if j%2==0:  # 偶数部分打印空格
            print(' ', end='')
        else:
            print('*', end='')
        j+=1
    print()
    i+=1