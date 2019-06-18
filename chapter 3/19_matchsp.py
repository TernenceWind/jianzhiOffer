# -*- coding:utf-8 -*-
# 正则表达式的匹配

class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if s == pattern:
            return True
        elif pattern == '':
            return False
        elif s == '':
            if pattern == '.':
                return False
            elif len(pattern) == 1 or pattern[1] != '*':
                return False
            else:
                return self.match(s, pattern[2:])
        if len(pattern) == 1:
            if len(s) == 1:
                if pattern == '.' or pattern == s:
                    return True
                else:
                    return False
            else:
                return False
        if pattern[1] != '*':
            if pattern[0] == '.' or pattern[0] == s[0]:
                return self.match(s[1:],pattern[1:])
            else:
                return False
        else:
            if pattern[0] != s[0] and pattern[0] != '.':
                return self.match(s,pattern[2:])
            else:
                return self.match(s[1:],pattern) or self.match(s,pattern[2:]) or self.match(s[1:],pattern[2:])