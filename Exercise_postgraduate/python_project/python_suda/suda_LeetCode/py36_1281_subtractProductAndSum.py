# -*- coding: utf-8 -*-
class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        from functools import reduce
        nstr = str(n)
        nint = list(map(int, nstr))
        
        pro = reduce(lambda x, y: x*y, nint)
        su = reduce(lambda x, y: x+y, nint)
        
        return pro - su
        
        
s = Solution()
print(s.subtractProductAndSum(234))
print(s.subtractProductAndSum(4421))
print(s.subtractProductAndSum(114))
        
        