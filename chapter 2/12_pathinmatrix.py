# coding = utf-8
# 矩阵中的路径

# -*- coding:utf-8 -*-
class Solution:
    def hasPath(self, matrix, rows, cols, path):
        # write code here
        assists = [True]*rows*cols
        for i in range(rows):
            for j in range(cols):
                if self.findPath(matrix, rows, cols, i, j, path, assists):
                    return True
        return False
    def findPath(self, matrix, rows, cols, i, j, path, assists):
        if not path:
            return True
        index = i * cols + j
        if i < 0 or i >= rows or j < 0 or j >= cols or matrix[index] != path[0] or assists[index] == False:
            return False
        assists[index] = False
        if self.findPath(matrix, rows, cols, i-1, j, path[1:], assists) or \
            self.findPath(matrix, rows, cols, i+1, j, path[1:], assists) or \
            self.findPath(matrix, rows, cols, i, j-1, path[1:], assists) or \
            self.findPath(matrix, rows, cols, i, j+1, path[1:], assists):
                return True
        assists[index] = True
        return False