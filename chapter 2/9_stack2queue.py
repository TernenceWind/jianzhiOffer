# coding = utf-8
# 用两个栈实现队列

# -*- coding:utf-8 -*-
class Solution:
    stack1 = []
    stack2 = []
    def push(self, node):
        # write code here
        self.stack1.append(node)
    def pop(self):
        # return xx
        if len(self.stack2) == 0:
            while self.stack1:
                self.stack2.append(self.stack1.pop())
        return self.stack2.pop()


# 用两个栈，queue的push操作只要往stack1里塞就行
# 出队列的时候，从stack2中出，如果stack2中出完了，就把stack1中存的数据反向怼到stack2中