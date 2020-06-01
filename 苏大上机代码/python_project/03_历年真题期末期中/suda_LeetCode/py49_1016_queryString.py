# -*- coding: utf-8 -*-

class Solution:
    def queryString(self, S: str, N: int) -> bool:
        for i in range(1, N+1):
            nbin = bin(i)[2:]
            if S.find(nbin) == -1:
                return False
        return True
    
s = Solution()
print(s.queryString('0110', 3))
print(s.queryString('0110', 4))
        