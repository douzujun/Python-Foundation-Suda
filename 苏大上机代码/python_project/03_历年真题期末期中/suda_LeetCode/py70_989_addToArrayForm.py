# -*- coding: utf-8 -*-

class Solution:
    def addToArrayForm(self, A, K: int):
        from functools import reduce
        a = reduce(lambda x, y:x*10+y, A)
        ans = a + K
        ans = list(map(int, list(str(ans))))
        return ans
    
s = Solution()
print(s.addToArrayForm(A = [1,2,0,0], K = 34))
print(s.addToArrayForm(A = [2,7,4], K = 181))
print(s.addToArrayForm(A = [2,1,5], K = 806))
print(s.addToArrayForm(A = [9,9,9,9,9,9,9,9,9,9], K = 1))

