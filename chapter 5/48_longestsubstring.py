# -*- coding:utf-8 -*-
# 最长不含重复字符的子字符串

# 借用字典
# 除此之外可用dp解决

class Solution:
    def lengthOfLongestSubstring(self, s):
        # write your code here
        res = 0
        if s is None or len(s) == 0:
            return res
        d = {}
        tmp = 0
        start = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                start = d[s[i]] + 1
            tmp = i - start + 1
            d[s[i]] = i
            res = max(res, tmp)
        return res

so = Solution()
a = 'ionfowieru'
print(so.lengthOfLongestSubstring(a))