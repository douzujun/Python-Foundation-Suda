# -*- coding: utf-8 -*-

class Solution:
    def isUgly(self, num: int) -> bool:
        if num == 0:
            return False
        if num == 1:
            return True
        elif num % 2 == 0:
            return self.isUgly(num // 2)
        elif num % 3 == 0:
            return self.isUgly(num // 3)
        elif num % 5 == 0:
            return self.isUgly(num // 5)
        else:
            return False
        

s = Solution()
print(s.isUgly(6))
print(s.isUgly(8))
print(s.isUgly(14))