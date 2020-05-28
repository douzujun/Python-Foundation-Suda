# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:32:01 2020

@author: douzi
"""

class Solution:
    def reverseWords(self, s: str) -> str:
        sli = s.split()
        
        res = []
        for word in sli:
            res.append(word[::-1])
        
        return ' '.join(res)
        
        
    
s = Solution()
print(s.reverseWords("Let's take LeetCode contest"))
        
