# coding = utf-8
# 旋转数组的最小数字


rotateArray = [2,2,2,2,2,3,4,1,2]
start, end = 0, len(rotateArray)-1
print(start,end)
if rotateArray[start]<rotateArray[end]:
    print(rotateArray[0])
    exit()
while start < end:
    mid = (start+end)//2
    print(start,end,mid)
    if rotateArray[mid] > rotateArray[start]:
        start = mid
    else:
        end = mid-1
print(start,end,mid)
print(rotateArray[start+1])