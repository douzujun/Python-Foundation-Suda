# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 19:47:00 2020

@author: douzi
"""

class Solution:
    def distributeCandies(self, candies) -> int:
        clen = len(candies) 
        ave = clen // 2
        
        cset = set()
        for e in candies:
            cset.add(e)
            if len(cset) == ave:
                break
        
#        print(cset)
        return len(cset)
    
s = Solution()
print(s.distributeCandies(candies = [1,1,2,2,3,3]))
print(s.distributeCandies(candies = [1,1,2,3]))
            
        
        