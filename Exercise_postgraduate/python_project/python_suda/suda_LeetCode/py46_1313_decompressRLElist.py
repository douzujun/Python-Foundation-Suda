# -*- coding: utf-8 -*-

class Solution:
    def decompressRLElist(self, nums):
        nlen = len(nums)
        points = [(nums[i], nums[i+1]) for i in range(0, nlen, 2)]

        res = []
        for e in points:
            freq = e[0]
            for i in range(freq):
                res.append(e[1])
            
        return res
    
s = Solution()
print(s.decompressRLElist([1, 2, 3, 4]))
