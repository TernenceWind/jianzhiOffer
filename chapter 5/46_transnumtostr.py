# _*_ coding:utf-8 _*_
# 把数组翻译成字符串


# 本题主要是动态规划的算法
# 注意状态转移

class Solution:
    def transnum(self, numbers):
        num = str(numbers)
        
        dp = [1 for i in range(len(num)+1)]
        for i in range(2,len(dp)):
            dp[i] = dp[i-1]
            temp = int(num[i-2:i])
            print(temp)
            if temp >= 10 and temp <= 25:
                dp[i] += dp[i-2]
        return dp[-1]


so = Solution()
print(so.transnum(10))