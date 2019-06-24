# -*- coding:utf-8 -*-
# 序列化二叉树


# 特别注意要有分隔符，因为单个节点的数值可能超过一个数字

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
class Solution:
    def Serialize(self, root):
        # write code here
        if not root:
            return '$'
        res = str(root.val)
        res += ','
        res += self.Serialize(root.left)
        res += ','
        res += self.Serialize(root.right)
        return res
    def Deserialize(self, s):
        # write code here
        serialize = s.split(',')
        tree, _ = self.des(serialize, 0)
        return tree

    def des(self, s, sp):
        if sp >= len(s) or s[sp] == '$':
            return None, sp+1
        node = TreeNode(int(s[sp]))
        sp += 1
        node.left, sp = self.des(s, sp)
        node.right, sp = self.des(s, sp)
        return node, sp
    


t = TreeNode(1)
t.left = TreeNode(2)
t.right = TreeNode(3)
t.left.left = TreeNode(4)
t.right.left = TreeNode(5)
t.right.right = TreeNode(6)

so = Solution()
print(so.Serialize(t))