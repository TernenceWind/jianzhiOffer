# coding = utf-8
# 机器人的运动范围

class Solution:
    assists = []
    def movingCount(self, threshold, rows, cols):
        # write code here
        count = 0
        self.assists = [True]*rows*cols
        count = self.movingCore(threshold, rows, cols, 0, 0, count)
        return count
    def sumation(self, num):
        add = 0
        while num // 10 != 0:
            add += (num % 10)
            num = (num // 10)
        add += num
        return add
    def movingCore(self, threshold, rows, cols, i, j, count):
        index = i * cols + j
        if i < 0 or j < 0 or i >= rows or j >= cols or self.assists[index] == False:
            return count
        if self.sumation(i) + self.sumation(j) > threshold:
            return count
        self.assists[index] = False
        print(i,j)
        count += 1
        count = self.movingCore(threshold, rows, cols, i-1, j, count)
        count = self.movingCore(threshold, rows, cols, i+1, j, count)
        count = self.movingCore(threshold, rows, cols, i, j-1, count)
        count = self.movingCore(threshold, rows, cols, i, j+1, count)
        return count

so = Solution()
print(so.movingCount(5,10,10))