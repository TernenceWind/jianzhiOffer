# -*- coding:utf-8 -*-
# 第一个只出现一次的字符


# 题目1：字符串中只出现一次的字符
class Solution:
    def FirstNotRepeatingChar(self, s):
        # write code here
        if len(s) == 0:
            return -1
        if len(s) == 1:
            return s
        chardic = dict()
        for i in s:
            if i not in chardic.keys():
                chardic[i] = 1
            else:
                chardic[i] += 1
        for i in range(len(s)):
            if chardic[s[i]] == 1:
                return i
        return -1


# 题目2：字符流中第一个只出现一次的字符
class Solution:
    def __init__(self):
        self.s = ''
        self.dict={}
    # 返回对应char
    def FirstAppearingOnce(self):
        # write code here
        for i in self.s:
            if self.dict[i] == 1:
                return i
        return '#'
    def Insert(self, char):
        # write code here
        self.s += char
        if char in self.dict.keys():
            self.dict[char] += 1
        else:
            self.dict[char] = 1