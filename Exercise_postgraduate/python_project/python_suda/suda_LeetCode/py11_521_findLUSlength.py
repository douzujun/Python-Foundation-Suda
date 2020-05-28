# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 00:01:16 2020

@author: douzi
"""

class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        return max(len(a), len(b)) if a != b else -1
        
    
s = Solution()
print(s.findLUSlength('aba', 'cdc'))