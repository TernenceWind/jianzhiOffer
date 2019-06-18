# -*- coding:utf-8 -*-
# 链表中倒数第k个结点

# 两个指针是一个思路，另一个思路是遍历一遍，把每个指针按顺序存入list中，然后直接去除倒数第k个
# 显然，两个算法的时间复杂度都是o(n)，但是空间复杂度上存入list的算法需要更多的额外存储空间

 class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def FindKthToTail(self, head, k):
        # write code here
        if k <= 0:
            return None
        if head == None:
            return head
        i = 0
        cur = head
        if k == 1:
            p_k = head
        else:
            p_k = None
        while cur.next:
            if i >= k-1:
                p_k = p_k.next
            cur = cur.next
            i = i + 1
            if i == k-1:
                p_k = head
        if p_k == None:
            return None
        else:
            return p_k