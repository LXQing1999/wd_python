"""
sort_arg 排序算法
Author:LXQing
Date:2023/7/5
"""
import random


class MySort:
    def __init__(self, list_len):
        self.arr = []
        self.arr_len = list_len  # 列表长度

    def random_int(self):
        for i in range(self.arr_len):
            self.arr.append(random.randint(0, 99))

    def bubble(self):
        arr = self.arr
        i = self.arr_len-1   # i是列表下标
        flag=True
        while i > 0 :
            j = 0
            while j < i:
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    flag =False
                j += 1
            i -= 1
            if flag==True:
                break

if __name__ == '__main__':
    temp = MySort(10)
    temp.random_int()
    print('自定义的随机列表', temp.arr)
