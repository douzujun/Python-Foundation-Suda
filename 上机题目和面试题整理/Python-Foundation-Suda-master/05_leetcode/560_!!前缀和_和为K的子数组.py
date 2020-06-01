"""
给定一个整数数组和一个整数 k，你需要找到该数组中和为 k 的连续的子数组的个数。

输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
"""
from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # 暴力法 超时
        current, ans = 0, 0
        for index in range(len(nums)):
            current = 0
            for num in nums[index::]:
                current += num
                if current == k:
                    ans += 1
        return ans


    def subarraySum2(self, nums: List[int], k: int) -> int:
        # 72ms 96% 前缀和 + 字典
        if len(nums) == 0:
            return 0
        prev_dict = {0 : 1}
        prev_sum, ans = 0, 0
        for num in nums:
            prev_sum += num
            if prev_dict.get(prev_sum-k):
                ans += prev_dict[prev_sum-k]
            prev_dict[prev_sum] =  prev_dict.get(prev_sum, 0) + 1
        return ans
                

if __name__ == "__main__":
    S = Solution()
    print(S.subarraySum2([1,1,1], 2))