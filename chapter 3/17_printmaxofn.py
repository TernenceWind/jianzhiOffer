# coding = utf-8
# 打印1到最大的n位数


def printmaxofn(n):
    if n == 0:
        return
    number = ['0'] * (n+1)
    number[-1] = '1'
    #printn(number)
    while number[0] == '0':
        printn(number)
        number = add_1(number)


def add_1(n):
    if ord(n[-1]) - ord('0') <= 8:
        n[-1] = chr(ord(n[-1])+1)
    elif ord(n[-1]) - ord('0') == 9:
        n = add_1(n[:-1]) + ['0']
    return n

def printn(n):
    n = ''.join(n)
    n = n.lstrip('0')
    print(n)

printmaxofn(2)