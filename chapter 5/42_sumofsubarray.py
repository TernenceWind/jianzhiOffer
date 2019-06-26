# -*- coding:utf-8 -*-
# 连续子数组的最大和

# 除此之外还可以考虑用动态规划实现



class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        if len(array) == 0:
            return 0
        lastpos = -1
        maxsum = 0
        currsum = 0
        maxint = array[0]
        for i in range(len(array)):
            if array[i] > maxint:
                maxint = array[i]
            if array[i] > 0:
                lastpos = i
                currsum = array[i]
                break
        curri = lastpos + 1
        while curri < len(array):
            if array[curri] > maxint:
                maxint = array[curri]
            currsum += array[curri]
            if array[curri] < 0:
                if (currsum - array[curri]) > maxsum:
                    maxsum = currsum - array[curri]
                if currsum <= 0:
                    currsum -= array[curri]
                    if currsum > maxsum:
                        maxsum = currsum
                    currsum = 0
            if array[curri] > 0:
                lastpos = curri
            curri += 1
        if lastpos == -1:
            return maxint
        for i in range(lastpos+1, len(array)):
            currsum -= array[i]
        if currsum > maxsum:
            maxsum = currsum
        return maxsum

so = Solution()
a = [-1,-1,-4,-3]
print(so.FindGreatestSumOfSubArray(a))
