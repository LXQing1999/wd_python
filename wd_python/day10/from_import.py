"""
from_import 导入部分函数模块,还可以重命名
Author:LXQing
Date:2023/7/2
"""
from test_module import say_hello as module_Dog
import random
module_Dog()
# say_hello()

print(random.randrange(1,9))
