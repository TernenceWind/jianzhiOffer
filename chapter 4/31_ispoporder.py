# -*- coding:utf-8 -*-
# 栈的压入弹出序列

# 构造一个辅助栈，模拟栈的压入弹出过程

class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        stack = []
        while popV:
            if stack and popV[0] == stack[-1]:
                popV.pop(0)
                stack.pop()
            elif pushV:
                stack.append(pushV.pop(0))
            else:
                return False
        return True