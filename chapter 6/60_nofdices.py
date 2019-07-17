# -*- coding:utf-8 -*-
# n个骰(tou)子的点数

# 第n个骰子得到k的次数由n-1个骰子 k-1 ~ k-6 的个数和所决定，动规递推式
# f(n,k) = f(n-1,k-1) + f(n-1,k-2) + f(n-1,k-3)+ f(n-1,k-4)+ f(n-1,k-5)+ f(n-1,k-6)
class Solution:
    def PrintProbability(self, n):
        dp = [[0 for i in range(6*n)] for i in range(n)]
        for i in range(6):
            dp[0][i] = 1
        for i in range(1,n):  #1，相当于2个骰子。
            for j in range(i,6*(i+1)):   #[0,i-1]的时候，频数为0（例如2个骰子不可能投出点数和为1）
                dp[i][j] = dp[i-1][j-6] + dp[i-1][j-5] + dp[i-1][j-4] +\
                            dp[i-1][j-3] + dp[i-1][j-2] + dp[i-1][j-1]

        count = dp[n-1]
        return count  #算得骰子投出每一个点数的频数。再除以总的排列数即可得到频率


so = Solution()
print(so.PrintProbability(6))