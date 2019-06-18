# -*- coding:utf-8 -*-
# 合并两个已排序的列表

# 首先找出第一项较小的为头，如果两个列表中任意一个走到头，即停止，若附加项没有走到头，则直接后缀到结果上即可


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        if pHead1 == None:
            return pHead2
        if pHead2 == None:
            return pHead1
        if pHead1.val > pHead2.val:
            pf = pHead2
            pl = pHead1
        else:
            pf = pHead1
            pl = pHead2
        pr = pf
        pfn = pf.next
        while pfn and pl:
            if pl.val <= pfn.val:
                plt = pl.next
                pf.next = pl
                pf.next.next = pfn
                pl = plt
                pf = pf.next
            else:
                pf = pf.next
                pfn = pfn.next
        if pfn == None:
            pf.next = pl
        return pr
node1 = ListNode(1)
node1.next = ListNode(3)
node1.next.next = ListNode(5)
node1.next.next.next = ListNode(7)
node1.next.next.next.next = ListNode(9)
node1.next.next.next.next.next = ListNode(11)
node1.next.next.next.next.next.next = ListNode(13)

node2 = ListNode(2)
node2.next = ListNode(4)
node2.next.next = ListNode(6)
node2.next.next.next = ListNode(8)
node2.next.next.next.next = ListNode(10)


so = Solution()
re = so.Merge(node1,node2)
while re:
    print(re.val)
    re = re.next