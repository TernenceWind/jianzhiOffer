# -*- coding:utf-8 -*-
# 股票的最大利润
# 股票只买卖一次所能获得的最大利润
class Solution:
    def maxProfit(self, prices: List[int]) -> int:                
        if len(prices) == 0:
            return 0
        maxp = 0
        minp = prices[0]
        for i in prices:
            if i < minp:
                minp = i
            else:
                diff = i-minp
                if diff > maxp:
                    maxp = diff
        return maxp
