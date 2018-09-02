# -*- coding:utf-8 -*-
'''合并排序:计算一个列表的中间位置，并用递归排序其左边和右边的子列表（分而治之）
将两个排好序的子列表重新合并为单个排好序的列表
当子列表不能再划分的时候，停止这个操作'''

# 合并函数
# a和b分别为左边列和右边列
def merge(a, b):
    lst = []
    j = h = 0
    # 仅当j和h下标在a，b内进行循环
    while j < len(a) and h < len(b):
        # 如果右边值大于左值，则将较小的值先添加进新列表
        if a[j] < b[h]:
            lst.append(a[j])
            # 添加完j下标增1进行下次比较
            j += 1
        else:
            # 若右边较小则先添加右边值
            lst.append(b[h])
            # 添加完后h增1，继续进行比较
            h += 1
    # 若a列被全部添加到新列表中（此时列表中全为较小值）
    # 则将b列中的h下标之后的值添加到新列表中完成排序
    if j == len(a):
        for i in b[h:]:
            lst.append(i)
    else:
        # 反之b中值被全部添加进新列表（此时列表中还全是最小值）
        # 则把a中j下标之后的值添加进新列表完成排序
        # 思路就是先添加小的值，后将大的值补齐
        for i in a[j:]:
            lst.append(i)
    # 返回新列表（排序的列表）
    return lst
# 使用函数的递归将列表分为最小项
def merge_sort(lyst):
    if len(lyst) <= 1:
        return lyst
    middle = len(lyst) / 2
    left = merge_sort(lyst[:middle])
    right = merge_sort(lyst[middle:])
    return merge(left, right)

print merge_sort([4, 1, 7, 6, 3, 8, 2])