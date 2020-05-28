# -*- coding: utf-8 -*-

class Solution:
    def arrayPairSum(self, nums) -> int:
        nums.sort()
        print(nums)
        
        rlen = len(nums)
        nums = [min(nums[i], nums[i+1]) for i in range(0, rlen-1, 2)]

        return sum(nums)
    
s = Solution()
print(s.arrayPairSum([1, 4, 3, 2]))
        
