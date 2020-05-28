# -*- coding: utf-8 -*-

class Solution:
    def maximumProduct(self, nums) -> int:
        nums.sort()
        return max(nums[-1]*nums[-2]*nums[-3],nums[-1]*nums[0]*nums[1])
    
s = Solution()
print(s.maximumProduct([-4,-3,-2,-1,60]))
print(s.maximumProduct([-1,-2,1,2,3]))
    
