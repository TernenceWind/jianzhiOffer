# -*- coding:utf-8 -*-
# 数字序列中某一位的数字

# 此题在牛客网网上找不到对应的题目

# 题目：数字以0123456789101112131415……的格式序列化到一个字符序列中。
# 在这个序列中，第5位（从0开始计数）是5，第13位是1，第19位是4，等等。
# 请写一个函数，求任意第n位对应的数字

class Solution:
    def findNthDigit(self, n: int) -> int:
        # 如果 n 小于 10 ，直接返回就可以了
        if n < 10:
            return n

        # 计算前缀部分

        base = 9
        digits = 1
        # 2 位数，从 10 到 99 一共 ( 99 - 10 + 1) * 2 = 90 * 2 = 180 位
        # 3 位数，从 100 到 999 一共 ( 999 - 100 + 1) * 2 = 900 * 3 = 2700 位
        # 4 位数，从 1000 到 9999 一共 ( 9999 - 1000 + 1) * 2 = 9000 * 4 = 3600 位

        while n - base * digits > 0:
            n -= base * digits
            base *= 10
            digits += 1


        index = n % digits
        if index == 0:
            # 计算出 num 是多少
            # 例如：192，有 1 个位移的偏差
            num = 10 ** (digits - 1) + n // digits - 1
            # 返回个位就可以了
            return num % 10
        else:
            # 不能整除，那个偏移就不用算了
            # 例如 194 = 189 + 5
            # 100 + 2 = 102
            num = 10 ** (digits - 1) + n // digits
            # 从左边向右边数，第 2 位
            for i in range(index, digits):
                num //= 10
            return num % 10