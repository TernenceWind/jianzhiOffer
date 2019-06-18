# -*- coding:utf-8 -*-
# 表示数值的字符串



class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        hasE = False
        sign = False
        decimal = False
        # 当字符串为空时，必不能表示数值
        if len(s) == 0:
            return False
        # 循环遍历字符串中的每一个字符
        for i in range(len(s)):
            if s[i]=="e" or s[i]=="E":
                if i==len(s)-1 or i == 0:
                    return False #e后面一定要有数字,第一位也不能是e
                if hasE:
                    return False #e只能有一个
                hasE = True
            elif s[i]=="+" or s[i]=="-":
                if sign and s[i-1] != "e" and s[i-1] != "E":  #第二次出现符号要紧跟e后面
                    return False
                if sign==False and i>0 and s[i-1] != "e" and s[i-1] != "E": #第一次出现符号，且不在开头，那么也要紧跟e后面
                    return False
                sign == True
            elif s[i]==".":
                if hasE or decimal: #小数点不在e后面且不能出现两次
                    return False
                decimal = True
            elif s[i]<"0" or s[i]>"9":
                return False
        return True