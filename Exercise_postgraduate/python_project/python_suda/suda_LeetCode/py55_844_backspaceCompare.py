# -*- coding: utf-8 -*-
"""
Created on Tue Apr 21 15:34:50 2020

@author: douzi
"""

class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        st1 = ''
        st2 = ''
        for e in S:
            if e != '#':
                st1 += e
            else:
                st1 = st1[:-1]
        for e in T:
            if e != '#':
                st2 += e
            else:
                st2 = st2[:-1]
                
        if st1 == st2:
            return True
        else:
            return False
    
s = Solution()
print(s.backspaceCompare(S = "ab##", T = "c#d#"))