# -*- coding:utf-8 -*-
# 不用加减乘除做加法
# python对位运算的设计
# 加法是异或 进位是<<1
# 要做越界检查
class Solution: 
    def Add(self, a, b):           
        while(b): 
            a,b = (a^b) & 0xFFFFFFFF,((a&b)<<1) & 0xFFFFFFFF
        return a if a<=0x7FFFFFFF else ~(a^0xFFFFFFFF)

