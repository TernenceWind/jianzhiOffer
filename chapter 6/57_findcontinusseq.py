# -*- coding:utf-8 -*-
# 和为s的数字



# 题目一： 和为s的连续正数序列
# 注意正数序列中至少要求包含两个元素，tsum = 1时结果应为空。
class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum <= 1:
            return []
        result = []
        head = 1
        end = 2
        cursum = 3
        mid = int((1+tsum)/2)
        while(head < mid):
            if tsum == cursum:
                result.append(self.sequence(head,end))
            while(cursum > tsum and head < mid):
                cursum -= head
                head += 1
                if tsum == cursum:
                    result.append(self.sequence(head,end))
            end += 1
            cursum += end
        return result
    
    def sequence(self, head, end):
        res = []
        for i in range(head,end+1):
            res.append(i)
        return res


# 题目二： 和为s的两个数字
class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        if not array:
            return []
        head = 0
        end = len(array)-1
        mproduct = 0
        result = []
        while(end > head):
            cursum = array[head]+array[end]
            if tsum == cursum:
                if len(result) == 0:
                    mproduct = array[head] * array[end]
                    result = [array[head], array[end]]
                else:
                    tproduct = array[head] * array[end]
                    if tproduct < mproduct:
                        mproduct = tproduct
                        result = [array[head], array[end]]
                head += 1
            elif tsum < cursum:
                end -= 1
            else:
                head += 1
        return result