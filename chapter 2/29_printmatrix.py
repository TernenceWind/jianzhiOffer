# -*- coding:utf-8 -*-
# 顺时针打印矩阵

# 此题由于下标变化剧烈，较为复杂
# 有一种解法是每次输出矩阵第一行，然后逆时针旋转矩阵，但是旋转矩阵的代价较大，不是很理想
# 本题算法为将一个闭合的圈子视作一个循环，有行走行有列走列，当整个矩阵为空时算法结束
# 此外，不建议都使用append进行添加元素，在大部分情况下均可整段添加

class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        if matrix == None:
            return []
        result = []
        while matrix:
            result += matrix.pop(0)
            if matrix and matrix[0]:
                for row in matrix:
                    result.append(row.pop())
            if matrix:
                result += matrix.pop()[::-1]
            if matrix and matrix[0]:
                for i in range(len(matrix)-1,0,-1):
                    result.append(matrix[i].pop(0))
        return result