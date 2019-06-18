# -*- coding:utf-8 -*-
# 删除有序链表中的重复节点
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def deleteDuplication(self, pHead):
        # write code here
        if pHead == None:
            return None
        if pHead.next == None:
            return pHead
        if pHead.val == pHead.next.val:
            cur = pHead.next
            while cur:
                if cur.val == pHead.val:
                    cur = cur.next
                else:
                    break
            return self.deleteDuplication(cur)
        pHead.next = self.deleteDuplication(pHead.next)
        return pHead

node1 = ListNode(1)
node1.next = ListNode(1)
node1.next.next = ListNode(1)
node1.next.next.next = ListNode(1)
node1.next.next.next.next = ListNode(1)
node1.next.next.next.next.next = ListNode(1)
node1.next.next.next.next.next.next = ListNode(2)

so = Solution()
re = so.deleteDuplication(node1)
while re:
    print(re.val)
    re = re.next