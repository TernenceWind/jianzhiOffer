# -*- coding:utf-8 -*-
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
        
        while pHead.next.next != None and pHead.val == pHead.next.val:
            pHead = pHead.next
        if pHead.next.next == None and pHead.val == pHead.next.val:
            return None
        tempp = pHead.next
        lastp = pHead
        llp = pHead       
        while tempp:
            if tempp.val == lastp.val:
                
            else:
                
        return pHead
node1 = ListNode(1)
node1.next = ListNode(2)
node1.next.next = ListNode(3)
node1.next.next.next = ListNode(3)
node1.next.next.next.next = ListNode(4)
node1.next.next.next.next.next = ListNode(4)
node1.next.next.next.next.next.next = ListNode(5)

so = Solution()
re = so.deleteDuplication(node1)
while re:
    print(re.val)
    re = re.next