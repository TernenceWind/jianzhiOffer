# -*- coding:utf-8 -*-
# 数据流中的中位数

# 此题构建一个最大堆和最小堆
# 较小的数值放在最大堆中，较大的数值放在最小堆中
# 动态微调两个堆的大小，让二者尽量平衡
# python中默认的堆是最小堆，通过存入对应的负值可改为最大堆



from heapq import *
class Solution:
    maxheap = []
    minheap = []
    totallen = 0
    def Insert(self, num):
        # write code here
        if len(self.maxheap) == 0 and len(self.minheap) == 0:
            self.totallen += 1
            heappush(self.maxheap, -num)
            return
        if num <= -self.maxheap[0]:
            heappush(self.maxheap, -num)
            self.totallen += 1
        else:
            if len(self.minheap) == 0:
                self.totallen += 1
                heappush(self.minheap, num)
                return
            else:
                if num > self.minheap[0]:
                    self.totallen += 1
                    heappush(self.minheap, num)
                else:
                    self.totallen += 1
                    heappush(self.maxheap, -num)
        if len(self.maxheap) - len(self.minheap) >= 2:
            heappush(self.minheap, -heappop(self.maxheap))
        elif len(self.minheap) - len(self.maxheap) >= 2:
            heappush(self.maxheap, -heappop(self.minheap))
    def GetMedian(self):
        # write code here
        if self.totallen % 2 == 0:
            return (self.minheap[0]-self.maxheap[0])/2.0
        else:
            if len(self.maxheap) > len(self.minheap):
                return -self.maxheap[0]
            else:
                return self.minheap[0]


so = Solution()
a = [5,2,3,4,1,6,7,0,8]
for i in a:
    so.Insert(i)
    print(so.maxheap)
    print(so.minheap)
    print(so.GetMedian())