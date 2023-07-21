"""
binary_search 二分查找
Author:LXQing
Date:2023/7/8
"""

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if target < arr[mid]:
            high = mid
        elif target > arr[mid]:
            low = mid
        else:  # 找到了最终位置
            return mid
    return -1

if __name__ == '__main__':
    arr = [30, 79, 75, 24, 95, 80, 32, 46, 89]
    print(binary_search(arr, 95))
