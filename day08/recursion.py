"""
recursion 递归
注意至少要有结束条件,避免栈溢出
动态规划的精髓:一个问题的解依附于其子问题的解
Author:LXQing
Date:2023/6/28
"""
def recur_sum(n):
    if n==1:
        return 1
    else:
        return n+recur_sum(n-1)
'''n个台阶,每次只能上一个或两个台阶,问有多少种走法'''
def step(n):
    if n==1 or n==2:
        return n
    else:
        return step(n-1)+step(n-2)
if __name__ == '__main__':
    print(recur_sum(100))
    print(step(13))