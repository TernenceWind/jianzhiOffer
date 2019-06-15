# -*- coding:utf-8 -*-
# 反转链表，返回反转后链表的头结点

# 为防止指针链断裂，采用三个指针同时跑的策略
# 需要在开始的地方考虑不足三个元素的情况

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead == None or pHead.next == None:
            return pHead
        p1 = pHead
        p2 = pHead.next
        if p2.next == None:
            p1.next = None
            p2.next = p1
            return p2
        p3 = pHead.next.next
        p1.next = None
        while p3:
            p2.next = p1
            p1 = p2
            p2 = p3
            p3 = p3.next
        p2.next = p1
        return p2