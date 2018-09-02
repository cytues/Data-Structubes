# -*- coding:utf-8 -*-
def insertion_sort(lyst):
    '''插入排序'''
    # 初始插入点
    i = 1
    while i < len(lyst):
        # 初始插入项
        item_to_insert = lyst[i]
        j = i - 1
        # 循环遍历所有在插入项之前的值
        while j >= 0:
            # 当插入项前的值大于插入项，则将之前值的后一项与其交换位置
            if item_to_insert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j -= 1
            else:
                break
        # 遍历搜索完所有的插入项之前项后，将插入项后移一位继续搜索
        lyst[j + 1] = item_to_insert
        i += 1
    return lyst


print insertion_sort([2, 5, 1, 4, 3])
