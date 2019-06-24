# -*- coding:utf-8 -*-
# 字符串的排列


# 题目中输入可能有重复的字符，并且最后的输出要按照字典序


class Solution:
    def Permutation(self, ss):
        # write code here
        if len(ss) <= 0:
            return []
        res = list()
        self.perm(ss, res, '')
        return sorted(list(set(res)))
        
    def perm(self, ss, res, path):
        if ss == '':
            res.append(path)
        else:
            for i in range(len(ss)):
                self.perm(ss[:i]+ss[i+1:],res,path+ss[i])
        