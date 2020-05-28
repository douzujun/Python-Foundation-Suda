# -*- coding: utf-8 -*-
class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # import math
        # if n <= 0:
        #     return False
        # ans = math.log(n, 3)
        # if n == 3**round(ans):
        #     return True
        # else:
        #     return False
        if n == 1:
            return True
        while n > 3:
            if n % 3 == 0:
                n //= 3
            else:
                break
        
        return n == 3

s = Solution()
print(s.isPowerOfThree(45))
print(s.isPowerOfThree(9))