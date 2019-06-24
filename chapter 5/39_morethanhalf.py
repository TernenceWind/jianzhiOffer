# -*- coding:utf-8 -*-
# 数组中出现次数超过一半的数字


# 利用字典进行统计
# 还用一种方法，设置一个计数器，遇到下一位与当前位相同就+1，不同就-1，从整体数量上来说
# 超过一半的数字必然是最后一个把次数设置为1的数字，最后做一次校验即可
# 感觉时间上并不如字典统计的方法
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here
        if not numbers:
            return 0
        tokens = {}
        half = int(len(numbers) / 2)
        for i in numbers:
            if i in tokens:
                tokens[i] += 1
                if tokens[i] > half:
                    return i
            else:
                tokens[i] = 1
                # 防止数组长度仅为1
                if tokens[i] > half:
                    return i
        return 0