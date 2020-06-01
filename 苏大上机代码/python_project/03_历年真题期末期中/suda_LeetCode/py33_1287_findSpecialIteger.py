# -*- coding: utf-8 -*-

class Solution:
    def findSpecialInteger(self, arr) -> int:
        alen = len(arr) // 4
        for e in arr:
            if arr.count(e) > alen:
                return e
    
s = Solution()
print(s.findSpecialInteger(arr = [1,2,2,6,6,6,6,7,10]))
        
