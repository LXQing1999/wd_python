"""
message
Author:LXQing
内部调用的时候打印了send和receive
但是它们返回了send和receive的
Date:2023/7/2
"""


def use_package():
    print(demo.message.send_message.send())
    print(demo.message.rec_message.receive())
if __name__ == '__main__':
    use_package()
