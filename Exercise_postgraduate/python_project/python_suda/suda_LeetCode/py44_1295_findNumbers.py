# -*- coding: utf-8 -*-

class Solution:
    def findNumbers(self, nums) -> int:
        res = 0
        for e in nums:
            estr = str(e)
            if len(estr) % 2 == 0:
                res += 1
        
        return res
    
    
s = Solution()
print(s.findNumbers(nums = [12, 345, 2, 6, 7896]))

print(s.findNumbers(nums = [555, 901, 482, 1771]))
        