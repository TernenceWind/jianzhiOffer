# -*- coding:utf-8 -*-
# 调整数组顺序，使奇数位于偶数前


# 此题书中与牛客网上的题设要求有所不同，书中仅要求奇数在前偶数在后
# 牛客网上还要求奇数内部的顺序不变，偶数内部的顺序也不变
# 本题给出的解决方案为牛客网上的答案
# 若按照书中的要求，本算法也可通过，但是另有更优的算法
# 同时从array的前后开始往中间找，左边遇到偶数就和右边遇到的奇数交换
# 一直到两边的查找汇合。此方法类似快速排序的第一轮。

class Solution:
    def iseven(self, n):
        if n % 2 == 0:
            return False
        else:
            return True
    def reOrderArray(self, array):
        # write code here
        i = 0
        even = []
        lena = len(array)
        while True:
            if i == len(array):
                break
            if self.iseven(array[i]):
                i = i + 1
            else:
                even.append(array.pop(i))
        return array+even
