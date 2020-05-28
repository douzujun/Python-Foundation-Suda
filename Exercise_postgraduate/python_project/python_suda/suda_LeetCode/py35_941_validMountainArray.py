# -*- coding: utf-8 -*-

class Solution:
    def validMountainArray(self, A) -> bool:
        i = 0
        alen = len(A)
        while i < alen-1 and A[i] < A[i + 1]:
            i = i + 1
        if i == 0:
            return False
        if i == alen-1:
            return False
        while i < alen-1 and A[i] > A[i + 1]:
            i = i + 1
        if i == alen - 1:
            return True
        else:
            return False
        
        
s = Solution()
print(s.validMountainArray([2, 1]))
print(s.validMountainArray([3, 5, 5]))

print(s.validMountainArray([0, 3, 2, 1]))
        
        
