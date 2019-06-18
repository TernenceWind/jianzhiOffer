# -*- coding:utf-8 -*-
# 之字形打印二叉树

# 再加一个辅助变量
# level 目前的层号
# 奇数层从左向右打印
# 偶数层从右向左打印



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Print(self, pRoot):
        # write code here
        result = []
        if pRoot == None:
            return result
        queue = [pRoot]
        level = 1
        temp = []
        nextlevel = 0
        tobeprinted = 1
        while queue:
            tq = queue.pop(0)
            temp.append(tq.val)
            tobeprinted -= 1
            if tq.left:
                queue.append(tq.left)
                nextlevel += 1
            if tq.right:
                queue.append(tq.right)
                nextlevel += 1
            if tobeprinted == 0:
                if level % 2 != 0:
                    result.append(temp)
                else:
                    result.append(temp[::-1])
                temp = []
                level += 1
                tobeprinted = nextlevel
                nextlevel = 0
        if len(temp) > 0:
            result.append(temp)
        return result