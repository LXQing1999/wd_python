"""
__init__ 是对外，打包运行时的一个桥梁

1.标识目录为Python包：
当一个目录下包含了__init__.py文件时，Python会将该目录视为一个包，
可以通过import语句导入其中的模块。

2.初始化包：__init__.py文件可以包含一些初始化代码，这些代码会在导入包时执行。
例如，可以在__init__.py文件中导入其他模块，定义包级别的变量或函数
Author:LXQing
Date:2023/7/2
"""
from . import rec_message
from . import send_message
