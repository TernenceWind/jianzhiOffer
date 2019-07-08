# -*- coding:utf-8 -*-
# 在排序数组中查找数字

# 此题用递归进行二分查找，用循环也可
class Solution:
    def dichotomy(self, data, k, start, end, type):
        if type == 0:
            # 找开始的地方
            if start > end:
                return None
            if data[start] == k and data[start-1] < k:
                return start
            else:
                mid = int((start+end)/2)
                if data[mid] < k:
                    return self.dichotomy(data, k, mid+1, end, type)
                elif data[mid] == k and data[mid-1] < k:
                    return mid
                else:
                    return self.dichotomy(data, k, start, mid-1, type)
        else:
            # 找结束的地方
            if start > end:
                return None
            if data[start] == k and data[start+1] > k:
                return start
            else:
                mid = int((start+end)/2)
                if data[mid] > k:
                    return self.dichotomy(data, k, start, mid-1, type)
                elif data[mid] == k and data[mid+1] > k:
                    return mid
                else:
                    return self.dichotomy(data, k, mid+1, end, type)
    def GetNumberOfK(self, data, k):
        # write code here
        if len(data) == 0:
            return None
        if data[0] == k:
            start = 0
        elif data[0] > k:
            return None
        else:
            start = self.dichotomy(data, k, 0, len(data)-1, 0)
        if data[-1] == k:
            end = len(data)-1
        elif data[-1] < k:
            return None
        else:
            end = self.dichotomy(data, k, 0, len(data)-1, 1)
        print(start, end)
        if start != None and end != None:
            return end - start + 1
        else:
            return 0







so = Solution()
a = [1,2,3,3,3,3,4,6]
b = [3,3,3,3,4,5]
c = [1,3,3,3,3,4,5]
d = []
k = 1
print(so.GetNumberOfK(c,0))