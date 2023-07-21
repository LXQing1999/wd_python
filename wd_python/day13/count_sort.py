"""
count_sort 计数排序
Author:LXQing
Date:2023/7/7
"""

import random
import time


class MySort:
    def __init__(self, list_len):
        self.arr = []
        self.arr_len = list_len  # 列表长度
        self.temp_arr = [0] * self.arr_len  # 初始化辅助数组
        self.boundary = 100  # 表示数据范围

    def random_int(self):
        for i in range(self.arr_len):
            self.arr.append(random.randint(0, self.boundary - 1))

    def count_sort(self):
        count = [0] * self.boundary  # 初始化
        i = 0
        arr = self.arr
        # 在该元素对应的,辅助数组的位置,+1
        while i < self.arr_len:
            count[arr[i]] += 1
            i += 1
        # 回填到原数组
        k = 0
        for i in range(self.boundary):
            j = 0
            # 下标i是原数组的元素值
            while j < count[i]:
                arr[k] = i
                k += 1
                j += 1

    # *args,**kwargs参数 前面有指针是因为一个是列表,一个是字典
    def test_sort_time(self, sort_method, *args, **kwargs):
        start = time.time()
        '''应该传入一个可调用的函数，而不是直接调用temp.count_sort(),这样会返回一个结果,就会报错'''
        sort_method(*args, **kwargs)
        end = time.time()
        print('用时:{}'.format(end - start))


if __name__ == '__main__':
    # 10000就有值了
    temp = MySort(10)
    temp.random_int()
    print('自定义的随机列表', temp.arr)
    temp.count_sort()
    print('计数排序后:', temp.arr)
    temp.test_sort_time(temp.count_sort)
