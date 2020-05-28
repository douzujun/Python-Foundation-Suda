# -*- coding: utf-8 -*-
class Solution:
    def countNegatives(self, grid) -> int:
        res = 0
        for ei in grid:
            for ej in ei:
                if ej < 0:
                    res += 1
        return  res

s = Solution()

print(s.countNegatives(grid = [[4,3,2,-1],[3,2,1,-1],[1,1,-1,-2],[-1,-1,-2,-3]]))