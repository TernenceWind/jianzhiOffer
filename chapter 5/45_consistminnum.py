# -*- coding:utf-8 -*-
# 把数组排成最小的数

# 本题的核心在于什么样的组合能构成最小的数
# 当mn < nm时，就应该打印出mn，即m小于n
# 所有的数字都排序完成，从小到大接一起就是最小的数
# 结论简单，证明很难


class Solution:
    def PrintMinNumber(self, numbers):
        # write code here
        def cmp(a, b):
            '''定义比较函数'''
            ab = int(a+b)
            ba = int(b+a)
            return 1 if ab > ba else -1
        string = [str(num) for num in numbers]
        string.sort(cmp, reverse=False)
        return ''.join(string)