# -*- coding: utf-8 -*-

class Solution:
#    输入：A = [1,1], B = [2,2]
#    输出：[1,2]
    def fairCandySwap(self, A, B):
        sa, sb = sum(A), sum(B)
        diff = (sa - sb) / 2
        A.sort()
        B.sort()
        i, j = 0, 0
        
        while A[i] - B[j] != diff:
            if A[i] - B[j] > diff:   # A[i] - B[j] > diff: j++
                j = j + 1
            if A[i] - B[j] < diff:
                i = i + 1
        
        return [A[i], B[j]]
            
    
    
    
s = Solution()
print(s.fairCandySwap(A = [1,1], B = [2,2]))
print(s.fairCandySwap(A = [1,2], B = [2,3]))
print(s.fairCandySwap(A = [2], B = [1,3]))
print(s.fairCandySwap(A = [1,2,5], B = [2,4]))
