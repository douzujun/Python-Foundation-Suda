# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 17:47:14 2020

@author: douzi
"""

class Solution:
    def projectionArea(self, grid):
        x_area = 0
        for x in grid:
            x = [e for e in x if e > 0]
            x_area += len(x)
        
        y_area = 0
        elems = list(zip(*grid))
        for e in elems:
            y_area += max(e)
            
        z_area = 0
        for e in grid:
            z_area += max(e)
        
        areas = x_area + y_area + z_area
        return areas

s = Solution()
print(s.projectionArea([[1,2], [3, 4]]))
print(s.projectionArea([[1,0], [0,2]]))