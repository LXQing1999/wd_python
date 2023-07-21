"""
merge_sort 归并排序
Author:LXQing
Date:2023/7/6
"""
import random


class MySort:
    def __init__(self, list_len):
        self.arr = []
        self.arr_len = list_len  # 列表长度
        self.temp_arr = [0] * self.arr_len  # 初始化

    def random_int(self):
        for i in range(self.arr_len):
            self.arr.append(random.randint(0, 99))

    # 合并数组
    def merge(self, low, mid, high):
        temp_arr = self.temp_arr
        arr = self.arr
        temp_arr[low:high + 1] = arr[low:high + 1]
        i = low
        j = mid+1
        k = low
        while i <= mid and j <= high:
            if temp_arr[i] < temp_arr[j]:
                arr[k] = temp_arr[i]
                k += 1
                i += 1
            else:
                arr[k] = temp_arr[j]
                k += 1
                j += 1
        while i <= mid:
            arr[k] = temp_arr[i]
            k += 1
            i += 1
        while j <= mid:
            arr[k] = temp_arr[j]
            k += 1
            j += 1

    def merge_sort(self, low, high):
        if low < high:
            mid = (low + high) // 2
            self.merge_sort(low, mid)
            self.merge_sort(mid + 1, high)
            # 合并两个有序数组
            self.merge(low, mid, high)


if __name__ == '__main__':
    temp = MySort(10)
    temp.random_int()
    print('自定义的随机列表', temp.arr)
    temp.merge_sort(0, temp.arr_len - 1)
    print(temp.arr)
