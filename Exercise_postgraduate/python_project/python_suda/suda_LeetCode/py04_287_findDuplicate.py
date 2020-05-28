# -*- coding: utf-8 -*-
"""
Created on Mon Apr 13 22:53:13 2020

@author: douzi
"""

class Solution:
    def findDuplicate(self, nums) -> int:
        for e in nums:
            if nums.count(e) > 1:
                return e
    
    
    
s = Solution()
print(s.findDuplicate([1, 3, 4, 2, 2]))

print(s.findDuplicate([3, 1, 3, 4, 2]))
        

        