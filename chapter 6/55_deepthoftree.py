# -*- coding:utf-8 -*-
# 二叉树的深度

# 第一小题 二叉树的深度
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    deepth = 0
    def Core(self, pRoot, k):
        if not pRoot:
            return
        if k > self.deepth:
            self.deepth = k
        self.Core(pRoot.left, k+1)
        self.Core(pRoot.right, k+1)
    def TreeDepth(self, pRoot):
        # write code here
        if not pRoot:
            return 0
        self.Core(pRoot, 1)
        return self.deepth


# 第二小题 平衡二叉树
# 判断一个二叉树是否是平衡二叉树
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Core(self, pRoot):
        if not pRoot:
            return 0
        l = self.Core(pRoot.left)
        r = self.Core(pRoot.right)
        if l == None or r == None:
            return None
        else:
            if l - r > -2 and l - r < 2:
                return max(l,r) + 1
            else:
                return None
    def IsBalanced_Solution(self, pRoot):
        # write code here
        if not pRoot:
            return True
        isbalance = self.Core(pRoot)
        if isbalance == None:
            return False
        else:
            return True