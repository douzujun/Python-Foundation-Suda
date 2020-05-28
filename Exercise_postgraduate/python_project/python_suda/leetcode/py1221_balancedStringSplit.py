# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 15:58:44 2020

@author: douzi
"""

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        ans = 0
        n = 0
        for e in s:
            ans = ans - 1 if e == 'L' else ans + 1
            if ans == 0:      # 模拟栈
                n += 1
        return n
    
s = Solution()
print(s.balancedStringSplit("RLLLLRRRLR"))
print(s.balancedStringSplit("RLRRLLRLRL"))