# -*- coding:utf-8 -*-
# 丑数 
class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        if index == 1:
            return 1
        uglylist = [1]
        t2 = 0
        t3 = 0
        t5 = 0
        for i in range(1, index):
            nextugly = min(uglylist[t2]*2, uglylist[t3]*3, uglylist[t5]*5)
            uglylist.append(nextugly)
            if nextugly == uglylist[t2]*2:
                t2 += 1
            if nextugly == uglylist[t3]*3:
                t3 += 1
            if nextugly == uglylist[t5]*5:
                t5 += 1
        return uglylist[-1]