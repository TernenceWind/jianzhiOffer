# -*- coding:utf-8 -*-
# 二叉树中和为某一值的所有路径

# 相关算法虽有不同，但本质基本上都是树的深度优先遍历中的前序遍历。

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def FindPath(self, root, expectNumber):
        # write code here
        result = []
        if not root:
            return result
        if root and not root.left and not root.right and root.val == expectNumber:
            return [[root.val]]
        left = self.FindPath(root.left, expectNumber-root.val)
        right = self.FindPath(root.right, expectNumber-root.val)
        for i in left + right:
            result.append([root.val]+i)
        return result