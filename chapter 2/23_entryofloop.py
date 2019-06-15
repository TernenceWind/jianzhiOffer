# -*- coding:utf-8 -*-
# 链表中环的入口结点

# 此题较为复杂，算法分三个部分
# 1 判断链表是否有环
# 2 判断环的长度
# 3 判断环的入口结点
# 
# 判断是否有环，用两个速度不一样的指针跑，如果两个指针指向了同一个，说明肯定有一个跑回头了，故有环
# 两个指针交会的地方肯定是环内，计数跑一圈，回到原地后可得环得大小
# 设计两个指针，让一个先跑一个环的长度，另一个跟着跑，两个第一次相遇则是环的入口


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def EntryNodeOfLoop(self, pHead):
        # write code here
        # 如果链表为空或只有一个节点，则一定无环
        if pHead == None or pHead.next == None:
            return None
        
        # 寻找环
        p1 = pHead
        p2 = pHead
        flag = False
        while p2:
            p1 = p1.next
            if p2.next:
                p2 = p2.next.next
            else:
                break
            if p2 == p1:
                flag = True
                break
        if flag == False:
            return None
        else:
            p_k = p1.next
            k = 1
            while p_k != p1:
                k = k + 1
                p_k = p_k.next
            # k为环的长度
            pf = pHead
            for i in range(k):
                pf = pf.next
            pl = pHead
            while pl != pf:
                pl = pl.next
                pf = pf.next
            return pl