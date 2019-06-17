# -*- coding:utf-8 -*-
# 对称的二叉树

# 有两个思路，其一根据前一题二叉树的镜像，首先翻转获取二叉树的镜像，再判断其与源二叉树是否完全相同
# 其二是对称二叉树在前序遍历时有特点，当二叉树完全对称，当前序遍历时调换左右子树的遍历顺序，其结果应完全相同
# 本题采用第二种思路


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def isSymmetrical(self, pRoot):
        # write code here
        if pRoot == None:
            return True
        return self.Compare(pRoot.left, pRoot.right)
    def Compare(self, left, right):
        if left == None:
            if right == None:
                return True
            else:
                return False
        if right == None:
            return False
        if left.val != right.val:
            return False
        return self.Compare(left.left, right.right) and self.Compare(left.right, right.left)
            