"""
error_line 
Author:LXQing
Date:2023/7/2
"""
try:
    print(a)
# Exception 是一个通用的异常类，可以捕获各种类型的异常。
except Exception as e:
    print(e)
    # e.__traceback__.tb_frame.f_globals 是一个包含全局变量的字典，其中包括 __file__ 变量，表示当前文件的路径。
    print('发生异常所在的文件',e.__traceback__.tb_frame.f_globals["__file__"])
    # 这是打印发生异常的代码行号的语句。e.__traceback__.tb_lineno 表示异常发生的代码行号。
    print('发生异常的代码',e.__traceback__.tb_lineno)
