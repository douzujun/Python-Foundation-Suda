# -*- coding: utf-8 -*-
"""
Created on Thu Apr 16 00:39:48 2020

@author: douzi
"""

class Solution:
    def titleToNumber(self, s: str) -> int:
        dic = {}
        for i in range(0, 26):
            dic[chr(ord('A')+i)] = i + 1
            
        res = 0
        slen = len(s)
        for i in range(slen):
            res += dic[s[i]] * 26**len(s[i+1:])
            
        return res
            
    
s = Solution()
print(s.titleToNumber('A'))
print(s.titleToNumber('AB'))
print(s.titleToNumber('ZY'))      
print(s.titleToNumber('AAA'))  
        