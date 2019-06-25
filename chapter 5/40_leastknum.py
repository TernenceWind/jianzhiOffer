# -*- coding:utf-8 -*-
# 最小的k个数

# 这个方法是先排序后取值，与书中所述的解法一不同，平均计算的话应该进行了多余的排序

class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        length = len(tinput)
        if length < k:
            return []
        start, end = 0, length-1
        tinput = self.partition(tinput, start, end)
        return tinput[:k]
    # 进行排序
    def partition(self, tinput, start, end):
        if start >= end:
            return tinput
        temp = tinput[start]
        i, j = start, end
        while i < j:
            while i < j and temp <= tinput[j]:
                j -= 1
            if i < j:
                tinput[i] = tinput[j]
                i += 1
            while i < j and temp > tinput[i]:
                i += 1
            if i < j:
                tinput[j] = tinput[i]
                j -= 1
        tinput[i] = temp
        self.partition(tinput, start, i-1)
        self.partition(tinput, i+1, end)
        return tinput

# 用python中的堆也可以做，python中的heapq是最小堆
'''
import heapq as hq
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # write code here
        length = len(tinput)
        if length < k:
            return []
        hq.heapify(tinput)
        res = []
        for i in range(k):
            res.append(hq.heappop(tinput))
        return res
'''

inputs = [3,6,4,1,6,7,4,8,9,3,4,2,7]
k = 5
so = Solution()
print(so.GetLeastNumbers_Solution(inputs,k))