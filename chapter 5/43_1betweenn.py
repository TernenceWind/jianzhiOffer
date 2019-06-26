# -*- coding:utf-8 -*-
# 1到n中1出现的个数

# 此题尚未理解

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n<1:
            return 0
        count = 0
        base = 1
        round = n
        while round>0 :
            weight = round%10
            round /= 10
            round = int(round)
            count += round*base
            if weight==1:
                count+=(n%base)+1
            elif weight>1:
                count += base
            base*=10
        return count
so = Solution()
print(so.NumberOf1Between1AndN_Solution(12345))