# -*- coding:utf-8 -*-
# 包含min函数的栈

# 设置一个辅助栈，其栈顶元素是当前时刻栈的最小值。辅助空间的最大值与原栈相同。

class Solution:
    stack = []
    minstack = []
    def push(self, node):
        # write code here
        self.stack.append(node)
        if self.min() == None or node < self.min():
            self.minstack.append(node)
    def pop(self):
        # write code here
        if self.stack:
            if self.stack[-1] == self.min():
                self.minstack.pop()
            return self.stack.pop()
        else:
            return None
    def top(self):
        # write code here
        if self.stack:
            return self.stack[-1]
        else:
            return None
    def min(self):
        # write code here
        if self.minstack:
            return self.minstack[-1]
        else:
            return None