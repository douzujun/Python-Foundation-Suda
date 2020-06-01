# -*- coding: utf-8 -*-

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        for i in range(1, num+1):
            if i**2 == num:
                return True
            elif i**2 > num:
                return False
            
s = Solution()
print(s.isPerfectSquare(16))
print(s.isPerfectSquare(1))