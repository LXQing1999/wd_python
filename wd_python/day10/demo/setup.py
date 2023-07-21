"""
setup.py
文件通常是在构建包或进行其他包相关操作时使用的
distutils是一个用于构建和安装Python模块的工具，需要安装，命令行
python setup.py install
python setup.py --help
Author:LXQing
Date:2023/7/2
"""
from distutils.core import setup

setup(name="message",
      version='1.0',
      description='发送和接受消息模块',
      long_description="完整的发送和接受消息模块",
      author="LXQing",
      author_email='',
      url='',
      py_modules=["message.send_message",
                  "message.rec_message"])

# setup(cmdclass={'install': None})
