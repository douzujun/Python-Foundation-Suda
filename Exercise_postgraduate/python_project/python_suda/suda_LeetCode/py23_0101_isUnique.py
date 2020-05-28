# -*- coding: utf-8 -*-

class Solution:
    def isUnique(self, astr: str):
        for e in astr:
            if astr.count(e) > 1:
                return False
        return True
    
    
s = Solution()
print(s.isUnique('leetcode'))
print(s.isUnique('abc'))

