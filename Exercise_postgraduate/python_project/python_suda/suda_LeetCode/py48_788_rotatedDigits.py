# -*- coding: utf-8 -*-

class Solution:
    def rotatedDigits(self, N: int) -> int:
        ans = 0
        
        for i in range(1, N+1):
            flag = False
            n = i
            while n:          # 1---N
                x = n % 10
                if x in [3, 4, 7]:
                    break
                elif x in [2, 5, 6, 9]:
                    flag = True
                n = n // 10
            if flag and n == 0:
                ans = ans + 1
                print(i)
            
        return ans

s = Solution()
print(s.rotatedDigits(10))

print(s.rotatedDigits(100))
        