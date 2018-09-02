# -*- coding:utf-8 -*-
from swap import swap

def bubble_sort(lyst):
    '''冒泡排序:依次将最大值往后移动达到排序的效果'''
    # 循环整个列表长度
    n = len(lyst)
    while n > 1:
        swapped = False
        i = 1
        while i < n:
            # 若前一项比后一项大，则将其往后移动
            # 通过循环逐次移动最大值到末尾
            if lyst[i] < lyst[i - 1]:
                swap(lyst, i, i - 1)
                swapped = True
            i += 1
        # 没有发生交换（列表是排好序的）则直接返回
        if not swapped: return
        n -= 1
        return lyst

print bubble_sort([7, 6, 1, 2, 5])
