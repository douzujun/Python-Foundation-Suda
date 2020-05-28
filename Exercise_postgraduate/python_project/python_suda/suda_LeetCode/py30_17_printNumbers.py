# -*- coding: utf-8 -*-

class Solution:
    def printNumbers(self, n: int) :
        res = list(range(1, 10**n))
        return res
    
s = Solution()
print(s.printNumbers(1))
print(s.printNumbers(2))
        