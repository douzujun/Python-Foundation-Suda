# -*- coding: utf-8 -*-
"""
Created on Wed Apr  1 16:22:59 2020

@author: douzi
"""

class Solution:
    def scoreOfParentheses(self, S: str) -> int:
        stack = []
        res = 0
        for i in S:
            if i == '(':
                stack.append(res)
                res = 0
            elif i == ')':
                p = stack.pop()
                res = p + 1 if res == 0 else p + 2 * res
            else:
                res += int(i)
        return res
                
                
s = Solution()
print(s.scoreOfParentheses('(())'))
print(s.scoreOfParentheses("(()(()))"))
print(s.scoreOfParentheses("()"))
