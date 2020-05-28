# -*- coding: utf-8 -*-

class Solution:
    def smallerNumbersThanCurrent(self, nums):
        res = [0] * len(nums)
        rlen = len(nums)
        for i in range(rlen):
            for j in range(rlen):
                if nums[i] > nums[j]:
                    res[i] += 1
        
        return res
        

s = Solution()

print(s.smallerNumbersThanCurrent(nums = [8,1,2,2,3]))

print(s.smallerNumbersThanCurrent(nums = [6,5,4,8]))

print(s.smallerNumbersThanCurrent(nums = [7,7,7,7]))

