# -*- coding:utf-8 -*-
# 分行从上到下打印二叉树

# 另加两个辅助变量
# tobeprinted 当前层尚未打印的数量
# nextlevel 下一层需要打印的数量



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表[[1,2],[4,5]]
    def Print(self, pRoot):
        # write code here
        result = []
        if pRoot == None:
            return result
        queue = [pRoot]
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
                result.append(temp)
                temp = []
                tobeprinted = nextlevel
                nextlevel = 0
        if len(temp) > 0:
            result.append(temp)
        return result