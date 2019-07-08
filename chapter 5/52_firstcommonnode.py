# -*- coding:utf-8 -*-
# 两个链表的第一个公共结点


# 每个结点只有一个next，从第一个公共结点开始，后面所有的结点都是公共结点
# 因此两个链表的长度差异仅存在于第一个公共结点之前。
# 计算两个链表的长度差，从长的链表先走长度差的距离，再共同向后遍历
# 第一个完全相同的链表就是第一个公共结点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        m = self.getLen(pHead1)
        n = self.getLen(pHead2)
        if m > n:
            for i in range(m-n):
                pHead1 = pHead1.next
        else:
            for i in range(n-m):
                pHead2 = pHead2.next
        while pHead1 != pHead2 and pHead1 and pHead2:
            pHead1 = pHead1.next
            pHead2 = pHead2.next
        return pHead1
    
    def getLen(self, pHead):
        length = 0
        while pHead:
            length += 1
            pHead = pHead.next
        return length