# -*- coding: utf-8 -*-
class Solution:
    def isValid(self, S: str) -> bool:
        while 'abc' in S:
            S = S.replace('abc', '')
        return not S
    
    
s = Solution()

print(s.isValid('aabcbc'))

print(s.isValid("abccba"))

print(s.isValid("abcabcababcc"))
        