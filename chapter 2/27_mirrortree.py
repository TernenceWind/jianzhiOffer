# -*- coding:utf-8 -*-
# 二叉树的镜像

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    # 返回镜像树的根节点
    def Mirror(self, root):
        # write code here
        if root == None:
            return None
        templ = self.Mirror(root.left)
        tempr = self.Mirror(root.right)
        root.left = tempr
        root.right = templ
        return root