# coding = utf-8
# 旋转数组的最小数字


class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        start, end = 0, len(rotateArray)-1
        while rotateArray[start] >= rotateArray[end]:
            if end - start == 1:
                return rotateArray[end]
            mid = (start+end)//2
            if rotateArray[start] == rotateArray[mid] == rotateArray[end]:
                return min(rotateArray[start:end+1])
            if rotateArray[mid] >= rotateArray[start]:
                start = mid
            if rotateArray[mid] <= rotateArray[end]:
                end = mid
        return rotateArray[end]