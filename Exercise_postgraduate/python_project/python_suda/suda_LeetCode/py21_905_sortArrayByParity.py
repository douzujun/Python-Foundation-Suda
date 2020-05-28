# -*- coding: utf-8 -*-

class Solution:
    def sortArrayByParity(self, A):
        i, j = 0, len(A)-1
        while i < j:
            while i < j and A[i] % 2 == 0:
                i = i + 1
            if i < j:
                t = A[i]
            while i < j and A[j] % 2 == 1:
                j = j - 1
            if i < j:
                A[i] = A[j]
                A[j] = t
        print(A)
        return A
    
    
s = Solution()
print(s.sortArrayByParity([3, 1, 2, 4]))
        