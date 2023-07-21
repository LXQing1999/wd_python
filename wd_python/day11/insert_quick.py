"""
insert_quick
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

    def insert(self):
        arr = self.arr
        i = 1
        while i < self.arr_len:
            insert_val = arr[i]
            j = i - 1
            while j>=0 and arr[j]>insert_val:
                if arr[j] < insert_val:
                    break
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = insert_val
            i+=1

    def partition(self,left,right):
        arr=self.arr
        k=left
        i=left
        while i<right:
            if arr[i]<arr[right]:
                arr[i],arr[k]=arr[k], arr[i]
                k+=1
            i+=1
        arr[k],arr[right]=arr[right],arr[k]
        return k



    def quick(self,left,right):
        if left<right:
            key=self.partition(left,right)
            self.quick(left,key-1)
            self.quick(right,key+1)


if __name__ == '__main__':
    temp = MySort(10)
    temp.random_int()
    print('自定义的随机列表', temp.arr)
    # temp.insert()
    # print(temp.arr)