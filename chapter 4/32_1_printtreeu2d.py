# -*- coding:utf-8 -*-
# 从上到下打印二叉树

# 即为二叉树的广度优先遍历



class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        result = []
        if root == None:
            return result
        queue = [root]
        while queue:
            temp = queue.pop(0)
            result.append(temp.val)
            if temp.left:
                queue.append(temp.left)
            if temp.right:
                queue.append(temp.right)
        return result