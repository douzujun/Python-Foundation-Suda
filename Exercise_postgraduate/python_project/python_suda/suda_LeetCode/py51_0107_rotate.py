# -*- coding: utf-8 -*-
class Solution:
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        N = len(matrix)
        
        #  matrix 顺时针转 90 度就是矩阵先上下翻转，后沿对角线翻转。
        matrix[:] = matrix[::-1]   # 先上下翻转
        for i in range(N):
            for j in range(i):
                # 沿对角线翻转
                matrix[j][i], matrix[i][j] = matrix[i][j], matrix[j][i]
        return matrix
        
s = Solution()
print(s.rotate(matrix = [[1,2,3],
                         [4,5,6],
                         [7,8,9]]))
        
#给定 matrix = 
#[
#  [1,2,3],
#  [4,5,6],
#  [7,8,9]
#],
#
#原地旋转输入矩阵，使其变为:
#[
#  [7,4,1],
#  [8,5,2],
#  [9,6,3]
#]
