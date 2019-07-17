# -*- coding:utf-8 -*-
# 构建乘积数组
# 提示:下三角和上三角
class Solution:
    def multiply(self, A):
        # write code here
        if not A:
            return
        B=[]
        n=len(A)
        k=1
        sum=1
        for i in A[1:n]:
            sum*=i
        B.append(sum)
        while k<n:
            sum=1
            for j in A[0:k]:
                sum*=j
            for j in A[k+1:n]:
                sum*=j
            B.append(sum)
            k=k+1
        return B
