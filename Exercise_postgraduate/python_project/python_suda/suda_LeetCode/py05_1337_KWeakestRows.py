# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 01:32:34 2020

@author: douzi
"""

class Solution:
    def kWeakestRows(self, mat, k: int): # -> List[int]:
        res = []
        mlen = len(mat)
        for i in range(mlen):
            res.append((mat[i].count(1), i))
            
        res.sort(key=lambda x:x[0])
        
        res = [e[1] for e in res[:k]]
        return res
    
s = Solution()
print(s.kWeakestRows(mat = [[1,1,0,0,0],
                            [1,1,1,1,0],
                            [1,0,0,0,0],
                            [1,1,0,0,0],
                            [1,1,1,1,1]], k = 3))
        
print(s.kWeakestRows(mat = [[1,0,0,0],
                            [1,1,1,1],
                            [1,0,0,0],
                            [1,0,0,0]], k = 2))
        