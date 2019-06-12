# coding = utf-8
# 整数的整数次方

# 此题可进一步优化，在幂运算时，若指数为4，直接循环需要乘4次底数
# 但4次方可以拆解成两个平方相乘，即可简化为3次乘法运算
# 只需处理指数的奇偶数以及正负号，可采用斐波那契数列的方法计算


# -*- coding:utf-8 -*-
class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0:
            return False
        if exponent == 0:
            return 1
        products = 1
        if exponent < 0:
            for i in range(-exponent):
                products *= base
            return (1.0/products)
        if exponent > 0:
            for i in range(exponent):
                products *= base
            return products