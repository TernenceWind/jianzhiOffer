# -*- coding:utf-8 -*-
# 数组中数字出现的次数


class Solution:
    # 返回[a,b] 其中ab是出现一次的两个数字
    def FindNumsAppearOnce(self, array):
        # write code here
        ans = [0,0]
        temp = 0
        # 求异或
        for e in array:
            temp ^= e
        # 寻找第一个为1的位
        idx = 0
        while (temp&1)==0 and idx<32:
            temp = temp>>1
            idx+=1
        # 分成两组，每组中各出一个单独的数字
        for e in array:
            if ((e>>idx)&1)==1:
                ans[0]=ans[0]^e
            else:
                ans[1] = ans[1]^e
        return ans

