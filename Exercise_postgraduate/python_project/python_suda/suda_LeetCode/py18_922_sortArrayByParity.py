# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 01:34:53 2020

@author: douzi
"""

class Solution:
    def sortArrayByParityII(self, A):
        Alen = len(A)
        res = [0] * Alen
        even, odd = 0, 1
        for e in A:
            if e % 2 == 0:
                res[even] = e
                even = even + 2
            else:
                res[odd] = e                
                odd = odd + 2
        print(res)
        return res
    
s = Solution()
print(s.sortArrayByParityII([4,2,5,7]))