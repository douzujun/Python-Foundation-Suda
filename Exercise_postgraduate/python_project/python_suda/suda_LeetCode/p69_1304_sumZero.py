# -*- coding: utf-8 -*-
class Solution:
    def sumZero(self, n: int):
        sum = 0
        ans = []
        for i in range(0, n-1):
            ans.append(i)
            sum += i
        ans.append(-sum)
        return ans

s = Solution()
print(s.sumZero(5))
print(s.sumZero(3))
print(s.sumZero(1))