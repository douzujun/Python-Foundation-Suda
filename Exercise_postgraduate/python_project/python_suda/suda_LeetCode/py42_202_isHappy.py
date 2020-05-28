# -*- coding: utf-8 -*-

class Solution:
    def isHappy(self, n: int) -> bool:
        from functools import reduce
        T = 10
        while T:
            nint = sum(map(lambda x:int(x)**2, str(n)))
            n = nint
            T = T - 1
        if n == 1:
            return True
        else:
            return False
            
s = Solution()
print(s.isHappy(19))