# -*- coding: utf-8 -*-
class Solution:
    def createTargetArray(self, nums, index):
        res = []
        nlen = len(nums)
        for i in range(nlen):
            res.insert(index[i], nums[i])
            
        return res
    
s = Solution()

print(s.createTargetArray(nums = [0,1,2,3,4], index = [0,1,2,2,1]))