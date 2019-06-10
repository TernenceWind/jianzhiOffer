# coding = utf-8
# 剪绳子

# 长度为n的绳子，剪成若干段
# 动态规划算法
def cutstrings_d(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2

    # 乘积
    products = [1] * (n+1)
    products[0] = 0
    products[1] = 1
    products[2] = 2
    products[3] = 3

    maxproduct = 0
    for i in range(4,n+1):
        maxproduct = 0
        for j in range(1,i//2+1):
            product = products[j] * products[i-j]
            if product > maxproduct:
                maxproduct = product
        products[i] = maxproduct
    return products[n]

# 长度为n的绳子，剪成若干段
# 贪婪算法
# 关键是为何拆解成长度为3的和2的
def cutstrings_t(n):
    if n < 2:
        return 0
    if n == 2:
        return 1
    if n == 3:
        return 2
    timesof3 = n // 3
    yushu = n - timesof3 * 3
    if yushu == 1:
        return ((3 ** (timesof3-1)) * 4)
    if yushu == 2:
        return ((3 ** timesof3) * 2)
    if yushu == 0:
        return (3 ** timesof3)



print(cutstrings_d(8))
print(cutstrings_t(8))
