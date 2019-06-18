# -*- coding:utf-8 -*-
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if not sequence:
            return False
        root = sequence[-1]
        # 小数取0，大数取1
        flag = 0
        seg = 0
        for s in sequence:
            if flag == 0:
                if s > root:
                    flag = 1
                    seg = sequence.index(s)
            elif flag == 1:
                if s < root:
                    return False
        if len(sequence[:seg]) > 0 and len(sequence[seg:-1]) >0:
            return self.VerifySquenceOfBST(sequence[:seg]) and self.VerifySquenceOfBST(sequence[seg:-1])
        elif len(sequence[:seg]) <= 0 and len(sequence[seg:-1]) >0:
            return self.VerifySquenceOfBST(sequence[seg:-1])
        elif len(sequence[:seg]) <= 0 and len(sequence[seg:-1]) >0:
            return self.VerifySquenceOfBST(sequence[:seg])
        else:
            return True

so = Solution()
print(so.VerifySquenceOfBST([4,8,6,12,16,14,10]))