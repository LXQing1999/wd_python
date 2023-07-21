"""
heap_sort 堆排
Author:LXQing
Date:2023/7/6
"""

import random


class MySort:
    def __init__(self, list_len):
        self.arr = []
        self.arr_len = list_len  # 列表长度

    def random_int(self):
        for i in range(self.arr_len):
            self.arr.append(random.randint(0, 99))

    # 调整大根堆
    def adjust_MaxHeap(self, father_pos, arr_len):
        arr = self.arr
        lchild_pos = 2 * father_pos + 1
        rchild_pos = 2 * father_pos + 2
        while lchild_pos < arr_len:
           # if arr[lchild_pos] < arr[rchild_pos] and rchild_pos < arr_len:
            if rchild_pos < arr_len and arr[lchild_pos] < arr[rchild_pos]:
                lchild_pos = rchild_pos
            if arr[lchild_pos] > arr[father_pos]:
                arr[lchild_pos], arr[father_pos] = arr[father_pos], arr[lchild_pos]
                father_pos = lchild_pos
                lchild_pos = 2 * father_pos + 1
            else:
                break

    def heap(self):
        # self.arr_len//2-1 最后一个根结点,结合二叉树的坐标来看
        arr = self.arr
        for i in range(self.arr_len // 2 - 1, -1, -1):
            self.adjust_MaxHeap(i, self.arr_len)
        # 调整后,最大的元素在树根,现在把它放到数组的最后去
        arr[0], arr[self.arr_len - 1] = arr[self.arr_len - 1], arr[0]
        for i in range(self.arr_len - 1, 0, -1):
            self.adjust_MaxHeap(0, i)
            arr[0], arr[i - 1] = arr[i - 1], arr[0]


if __name__ == '__main__':
    temp = MySort(10)
    temp.random_int()
    print('自定义的随机列表', temp.arr)
    temp.heap()
    print(temp.arr)