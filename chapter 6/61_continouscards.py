# -*- coding:utf-8 -*-
# 扑克牌中的顺子
class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if numbers == []:
            return False
        numbers.sort()
        nof0 = 0
        for i in numbers:
            if i == 0:
                nof0 += 1
            else:
                break
        if nof0 == len(numbers) or nof0 == len(numbers)-1:
            return True
        for i in range(nof0+1, len(numbers)):
            dv = numbers[i] - numbers[i-1] - 1
            if dv == -1:
                return False
            nof0 -= dv
            if nof0 < 0:
                return False
        return True


so = Solution()
array = [3,2,6,4]
print(so.IsContinuous(array))