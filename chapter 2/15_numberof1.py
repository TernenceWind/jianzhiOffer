# coding = utf-8
# 二进制中1的个数


# Python 2 的数值类型 int 是普通整型，是有范围的，可以通过 sys.maxint 获取其最大值，
# 至少 32 bit。当 Python 2 程序中的整数值超出范围后，自动转换为 long 类型，而 long 类
# 型是没有范围限制的，即 unlimited precision。在 Python 3 中，这两种类型被统一起来，
# 表示为 int 类型，与 Python 2 的数值类型 long 相同，没有范围限定（unlimited precision）。
# 也就是说，在 Python 中，整型数是没有溢出的（overflow）。在 Python 程序中，当对一个负
# 整数与其减 1 后的值按位求与，若结果为 0 退出，循环执行此过程。由于整型数可以有无限的数
# 值精度，其结果永远不会是 0，如此编程，在 Python 中，只会造成死循环。

def NumberOf1(n):
        # write code here
        if n < 0:
            n = n & 0xffffffff
        count = 0
        while n:
            count += 1
            n = (n-1) & n
        return count

print(NumberOf1(-1))

