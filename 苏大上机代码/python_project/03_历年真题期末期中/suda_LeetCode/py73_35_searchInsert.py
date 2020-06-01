# -*- coding: utf-8 -*-

class Solution:
    def searchInsert(self, nums, target: int) -> int:
        nlen = len(nums)
        if nlen == 0:
            return 0
        if target < nums[0]:
            return 0
        if target > nums[nlen - 1]:
            return nlen
        low, high = 0, nlen - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                high = mid - 1
            else:
                high = mid + 1
                
        return low
        
    
s = Solution()
#print(s.searchInsert([1,3,5,6], 5))
#print(s.searchInsert([1,3,5,6], 7))
print(s.searchInsert([1], 0))
        
        