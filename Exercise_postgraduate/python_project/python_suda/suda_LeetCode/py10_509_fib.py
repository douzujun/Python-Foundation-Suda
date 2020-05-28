# -*- coding: utf-8 -*-
"""
Created on Tue Apr 14 23:18:24 2020

@author: douzi
"""

class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        
        a, b = 0, 1
        c = 0
        for i in range(N-1):
            c = a + b
            a = b
            b = c
        return c
    
s = Solution()
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))