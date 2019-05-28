# coding = utf-8
# 数组中的重复数字

a = [2,3,1,0,6,5,4]
for i in range(len(a)):
    if a[i] == i:
        continue
    elif a[i] == a[a[i]]:
        print(a[i])
    else:
        k = a[i]
        a[i], a[k] = a[k], a[i]
        i = i - 1