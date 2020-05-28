# 102850211815667-窦祖俊
# -*- coding: utf-8 -*-

class Solution:
    def subarraySum(self, nums, k: int) -> int:
        ans = 0
        sum = 0
        hash = {0 : 1}
        nlen = len(nums)
        for i in range(nlen):
            sum += nums[i]
            if ((sum - k) in hash):
                ans += hash[sum - k]     # +1
            if (sum in hash):            # sum == 0
                hash[sum] += 1           # 如果sum 能加出 hash中的key， 则对应key的value+1
            else:
                hash[sum] = 1

        return ans
    
s = Solution()

print(s.subarraySum(nums = [1,1,1], k = 2))
print(s.subarraySum([28,54,7,-70,22,65,-6], 100))