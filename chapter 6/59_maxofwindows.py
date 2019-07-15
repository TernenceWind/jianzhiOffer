# -*- coding:utf-8 -*-
# 滑动窗口的最大值
class Solution:
    def findmax(self, num):
        maxnum = 0
        nummax = 0
        for i in num:
            if nummax == 0:
                maxnum = i
                nummax = 1
            else:
                if i > maxnum:
                    maxnum = i
                    nummax = 1
                elif i == maxnum:
                    nummax += 1
        return maxnum, nummax
    def maxInWindows(self, num, size):
        # write code here
        if len(num) == 0:
            return []
        if size == 0:
            return []
        if size > len(num):
            return []
        maxofnum, numofmax = self.findmax(num[:size])
        result = [maxofnum]
        head = 0
        end = size
        while(end < len(num)):
            if num[head] == maxofnum:
                numofmax -= 1
                if numofmax == 0:
                    maxofnum, numofmax = self.findmax(num[head+1:end+1])
            elif num[end] == maxofnum:
                numofmax += 1
            elif num[end] > maxofnum:
                maxofnum = num[end]
                numofmax = 1
            result.append(maxofnum)
            head += 1
            end += 1

        return result
so = Solution()
num = [2,3,4,2,6,2,5,1]
size = 3
print(so.maxInWindows(num,size))