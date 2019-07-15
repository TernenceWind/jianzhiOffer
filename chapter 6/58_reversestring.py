# -*- coding:utf-8 -*-
# 翻转字符串


# 题目一： 翻转单词顺序
# 方法一：不考虑复杂度问题，最简单的方法
class Solution:
    def ReverseSentence(self, s):
        # write code here
        split = s.split(' ')
        return ' '.join(split[::-1])
# 方法二：遍历一遍即可，时间复杂度为o(n)
class Solution:
    def ReverseSentence(self, s):
        # write code here
        result = ""
        temps = ""
        for i in s:
            if i == ' ':
                result = temps + ' ' + result
                temps = ""
            else:
                temps += i
        result = temps + ' ' + result
        return result[:-1]

# 题目二： 左旋转字符串
# 方法一： 直接做字符串拼接
class Solution:
    def LeftRotateString(self, s, n):
        # write code here
        if len(s) == 0:
            return s
        n = n % len(s)
        return s[n:]+s[:n]
# 方法二：模拟了剑指offer中的两次翻转的方法
# 因为是模拟的，介于python语言的特点，其实并不优于方法一
class Solution:
    def reverse(self, s):
        if not s:
            return ""
        length = len(s)
        if length <= 0:
            return ""
        s = list(s)
        #print s
        start = 0
        end = length - 1
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1
        #print 'after', s
        return ''.join(s)
    def LeftRotateString(self, s, n):
        # write code here
        if not s:
            return ""
        length = len(s)
        if length <= 0:
            return ""
        if n > length:
            n = n % length
        s = self.reverse(s)
        first = self.reverse(s[:-n])
        second = self.reverse(s[-n:])
        return first + second