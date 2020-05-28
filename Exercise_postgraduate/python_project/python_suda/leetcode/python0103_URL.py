# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 00:35:08 2020

@author: douzi
"""

class Solution:
    def replaceSpaces(self, S: str, length: int) -> str:
        S = S[:length].replace(' ', '%20')
        return S
    
    

s = Solution()
print(s.replaceSpaces("Mr John Smith    ", 13))
        
        