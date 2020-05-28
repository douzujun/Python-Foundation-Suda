# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:26:17 2020

@author: douzi
"""

class Solution:
    def generateParenthesis(self, n: int):
        res = []
        state = ''
        
        def dsp(state, p, q):
            if p > q:
                return
            if q == 0:
                res.append(state)
                
            if p > 0:         # p == q时候, 则递归搜索 
                dsp(state + '(', p - 1, q)
            if q > 0:
                dsp(state + ')', p, q - 1)
        
        dsp(state, n, n)
        return res
    
s = Solution()
print(s.generateParenthesis(3))
print(s.generateParenthesis(4))
