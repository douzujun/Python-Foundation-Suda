# -*- coding: utf-8 -*-
class Solution:
    def subsets(self, nums):
#        res = [[]]
#        
#        for i in nums:
#            print(i)
#            res = res + [[i] + num for num in res]
#        return res
        res = []
        nlen = len(nums)
        
        def dfs(i, tmp):
            res.append(tmp)
            for j in range(i, nlen):
                dfs(j + 1, tmp + [nums[j]])
        
        dfs(0, [])
        return res
        
s = Solution()

print(s.subsets([1,2,3]))
