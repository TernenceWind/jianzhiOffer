# -*- coding:utf-8 -*-
# 二叉树中第k大结点

# 此题在牛客网上没有对应的题目，但是在leetcode上有极为类似的题目
# 题目编号为230 题目内容为：二叉搜索树中第K小的元素
# 下面的代码为leetcode上通过的代码


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    arraylist = []
    def core(self, root: TreeNode, k: int):
        if len(self.arraylist) == k:
            return
        if not root:
            return
        self.core(root.left,k)
        self.arraylist.append(root.val)
        self.core(root.right,k)
            
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        if not root or k == 0:
            return None
        self.core(root, k)
        if len(self.arraylist) < k:
            return None
        else:
            return self.arraylist[k-1]