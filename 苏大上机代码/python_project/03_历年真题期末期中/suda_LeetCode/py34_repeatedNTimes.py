# -*- coding: utf-8 -*-
class Solution:
    def repeatedNTimes(self, A) -> int:
        for e in A:
            if A.count(e) > 1:
                return e
            
    
    
s = Solution()
print(s.repeatedNTimes([1, 2, 3, 3]))
print(s.repeatedNTimes([2, 1, 2, 5, 3, 2]))
print(s.repeatedNTimes([5,1,5,2,5,3,5,4]))