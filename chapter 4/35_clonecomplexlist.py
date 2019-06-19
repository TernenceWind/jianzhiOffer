# -*- coding:utf-8 -*-
# 复杂链表的复制

# 分三步
# 第一步首先在原位置后接上被复制的结点
# 第二步则顺序修改所有的随即指针
# 第三步是将复制的结果摘出来

class RandomListNode:
    def __init__(self, x):
        self.label = x
        self.next = None
        self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):
        # write code here
        self.CloneNode(pHead)
        self.CloneRandom(pHead)
        return self.SplitClone(pHead)
    def CloneNode(self, pHead):
        tp = pHead
        while tp:
            pClone = RandomListNode(tp.label)
            pClone.next = tp.next
            tp.next = pClone
            tp = pClone.next
    def CloneRandom(self, pHead):
        tp = pHead
        while tp:
            if tp.random:
                tp.next.random = tp.random.next
            tp = tp.next.next
    def SplitClone(self, pHead):
        tp = pHead
        pcHead = None
        pcNode = None
        if tp != None:
            pcNode = pcHead = tp.next
            tp.next = pcNode.next
            tp = tp.next
        while tp!= None:
            pcNode.next = tp.next
            pcNode = pcNode.next
            tp.next = pcNode.next
            tp = tp.next
        return pcHead



so = Solution()

pHead = RandomListNode(1)
pHead.next = RandomListNode(2)
pHead.next.next = RandomListNode(3)
pHead.next.next.next = RandomListNode(4)
pHead.next.next.next.next = RandomListNode(5)
pHead.next.next.next.next.next = RandomListNode(6)
pHead.next.next.next.next.next.next = RandomListNode(7)
pHead.next.next.next.next.next.next.next = RandomListNode(8)
pHead.next.next.next.next.next.next.next.next = RandomListNode(9)
pHead.next.next.next.next.next.next.next.next.next = RandomListNode(10)

pHead.random = pHead
pHead.next.random = pHead.next
pHead.next.next.random = pHead.next.next
pHead.next.next.next.random = pHead.next.next.next
pHead.next.next.next.next.random = pHead.next.next.next.next
pHead.next.next.next.next.next.random = pHead.next.next
pHead.next.next.next.next.next.next.random = pHead.next.next.next.next
pHead.next.next.next.next.next.next.next.random = None
pHead.next.next.next.next.next.next.next.next.random = pHead.next
pHead.next.next.next.next.next.next.next.next.next.random = None

re = so.Clone(pHead)
while re:
    print(re.label)
    if re.random:
        print('*',re.random.label)
    else:
        print('*',None)
    re = re.next