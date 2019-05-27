# coding = utf-8
# 二叉树的下一个节点

class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

def GetNext(pNode):
    if not pNode:
        return None
    if pNode.right:
        return findleft(pNode.right)
    elif pNode.next and pNode.next.left == pNode:
        return pNode.next
    elif pNode.next and pNode.next.right == pNode:
        return findright(pNode.next)
    elif not pNode.next:
        return None
        
def findleft(pNode):
    if pNode.left:
        return findleft(pNode.left)
    else:
        return pNode
def findright(pNode):
    if pNode == None:
        return None
    if pNode.next and pNode.next.right == pNode:
        return findright(pNode.next)
    if pNode.next and pNode.next.left == pNode:
        return pNode.next
    if not pNode.next:
        return None