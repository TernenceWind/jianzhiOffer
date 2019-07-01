# -*- coding:utf-8 -*-
# 礼物的最大价值


class Solution:
    def getMaxValue(self, values):
        if not values:
            return 0
        rows = len(values)
        cols = len(values[0])
        maxValue = [0]*cols
        for i in range(rows):
            for j in range(cols):
                left = 0
                up = 0
                if i > 0:
                    up = maxValue[j]
                if j > 0:
                    left = maxValue[j-1]
                maxValue[j] = max(left, up) + values[i][j]
        return maxValue

a = [[1,10,3,8],[12,2,9,6],[5,7,4,11],[3,7,16,5]]

so = Solution()
print(so.getMaxValue(a))