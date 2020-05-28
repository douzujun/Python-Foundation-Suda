# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 20:56:53 2020

@author: douzi
"""
#输入: 5
#输出:
#[
#     [1],
#    [1,1],
#   [1,2,1],
#  [1,3,3,1],
# [1,4,6,4,1]
#]
class Solution:
    def generate(self, numRows: int):
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1], [1, 1]]
        res = [[] for i in range(numRows)]
        res[0].append(1)
        res[1] = [1, 1]
        
        print(res)
        cnt = 1
        for i in range(2, numRows):
            res[i].append(1)
            for j in range(cnt):
                res[i].append(res[i-1][j] + res[i-1][j+1])
            res[i].append(1)
            cnt = cnt + 1

        print(res)
        return res
        
        
s = Solution()
print(s.generate(2))
print(s.generate(5))