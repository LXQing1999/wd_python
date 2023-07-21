"""
bitmap 位图去重 int
Author:LXQing
Date:2023/7/8
"""
class Bitmap:
    def __init__(self):
        self.bitmap=0
        self.arr=[84, 70, 59, 97, 59, 13, 70, 59, 13, 0]
        print('原代码',self.arr)
        self.newarr=[]
    def nodup(self):
        for i in self.arr:
            if self.bitmap& (1<<i): # 左移  按位与 1&1=1 表示已经出现过，pass
                pass
            else:
                self.newarr.append(i)
                self.bitmap|=1<<i

if __name__ == '__main__':
    b=Bitmap()
    b.nodup()
    print('去重后',b.newarr)