# -*- coding:utf-8 -*-
def binary_search(target, sortedLyst):
    '''二叉搜索：仅针对排好序的列表'''
    left = 0
    right = len(sortedLyst) - 1
    # 当左边不等于右边时循环进行
    while left < right:
        # 求中点
        midpoint = (left + right) // 2
        # 若目标恰好为中间值则返回中值位置
        if target == sortedLyst[midpoint]:
            return midpoint
        # 若目标比中间值大，则将范围向左缩小
        elif target < sortedLyst[midpoint]:
            right = midpoint - 1
        # 若目标比中间值小，则将范围向右缩小
        else:
            left = midpoint + 1
    # 上述情况没有找到目标则返回-1（目标不存在）
    return -1

print binary_search(6, [1, 3, 5, 6, 8])