# -*- coding:utf-8 -*-
from swap import swap

def selecttion_sort(lyst):
    '''选择排序：依次将最小的数往前移动'''
    i = 0
    # 做n - 1次查找
    while i < len(lyst) - 1:
        # 默认最小项为第一项
        min_index = i
        j = i + 1
        # 仅当后一项的位置不超过列表长度时搜索
        # 找出列表中最小的值
        while j <len(lyst):
            # 如果出现比最小值还要小的数，替换
            if lyst[j] < lyst[min_index]:
                min_index = j
            # 1轮循环过后向后移动一位
            j += 1
        # 搜索结束之后如果最小值不在第一位则交换最小值位置
        if min_index != i:
            swap(lyst, min_index, i)
        i += 1
    return lyst

print selecttion_sort([5, 3, 2, 1, 4])