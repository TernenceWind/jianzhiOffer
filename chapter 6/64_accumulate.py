# -*- coding:utf-8 -*-
# 计算1+2+3+······+n
# 要求： 不能用乘除法，for while if else 等关键字以及A？B:C
class Solution:
    def Sum_Solution(self, n):
        # write code here
        return n>0 and (n+self.Sum_Solution(n-1))
so = Solution()
print(so.Sum_Solution(3))