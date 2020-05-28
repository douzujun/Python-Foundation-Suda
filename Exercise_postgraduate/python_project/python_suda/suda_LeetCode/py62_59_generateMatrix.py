# -*- coding: utf-8 -*-

class Solution:
    def generateMatrix(self, n: int):
        matrix = [[0]*n for i in range(n)]
        
        num, tar = 1, n*n
        left, right = 0, n-1
        top, bottom = 0, n-1
        while num <= tar:
            # 左-->右
            for i in range(left, right + 1):
                matrix[top][i] = num
                num = num + 1
            top = top + 1
            # 上-->下
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num = num + 1
            right = right - 1
            # 右-->左
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num = num + 1
            bottom = bottom - 1
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num = num + 1
            left = left + 1
        
        return matrix
    
s = Solution()
print(s.generateMatrix(3))
        
        