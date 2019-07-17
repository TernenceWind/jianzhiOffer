# -*- coding:utf-8 -*-
# 圆圈最后剩下的数字
# 即约瑟夫环问题
# 两个思路，其一是模拟删除过程
# 第二个是寻找被删除的数字的规律，直接计算最后剩下的数字
class Solution:
    def LastRemaining_Solution(self, n, m):
        # write code here
        if n < 1 or m < 1:
            return -1
        last = 0
        for i in range(2,n+1):
            last = (last+m)%i
        return last