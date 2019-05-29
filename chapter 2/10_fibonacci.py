# coding = utf-8
# 斐波那契数列


class Solution:
    def Fibonacci(self, n):
        # write code here
        fn = []
        for i in range(n+1):
            if i == 0:
                fn.append(0)
            elif i == 1:
                fn.append(1)
            else:
                fn.append(fn[i-1]+fn[i-2])
        return fn[-1]