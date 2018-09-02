# -*- coding:utf-8 -*-
'''快速排序：快速排序的主要思想就是分而治之，
在基准点的左右两边分割列表形成子列表，递归的
重复应用该过程，左边为较小的项，而右边为较大的项'''
import random
from swap import swap

def quicksort(lyst):
    quicksort_helper(lyst, 0, len(lyst) - 1)

def quicksort_helper(lyst, left, right):
    if left < right:
        # 从partition函数得到基准点
        pivot1 = partition(lyst, left, right)
        # 使用递归细分左边和右边的列表
        quicksort_helper(lyst, left, pivot1 - 1)
        quicksort_helper(lyst, pivot1 + 1, right)

def partition(lyst, left, right):
    # 中点位置
    middle = (left + right) // 2
    # 在中点位置选择一项做为基准点
    piovt2 = lyst[middle]
    # 将基准点和最后一项交换
    lyst[middle] = lyst[right]
    lyst[right] = piovt2
    # 在第一项之前设置一个边界
    boundary = left
    # 扫描小于基准点的第一项
    # 循环直到所有比基准点小的项都移到了左边
    for index in range(left, right):
        if lyst[index] < piovt2:
            # 若找到比基准点小的项则于边界之后的第一项交换
            swap(lyst, index, boundary)
            # 边界后移
            boundary += 1
    # 将所有比基准点大的值移到右边
    swap(lyst, right, boundary)
    # 返回边界值（此时边界应该在基准值的位置上）
    return boundary

def main(size = 20, sort = quicksort):
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    print(lyst)
    sort(lyst)
    print(lyst)

if __name__ == '__main__':
    main()

