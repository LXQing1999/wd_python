"""
python传参
用命令行传递给你的程序的参数
Author:LXQing
Date:2023/07/29
"""
import sys
# sys.argv变量是一个字符串列表，用命令行传递给你的程序的参数。外部传参
for i in sys.argv:
    print(i)
