"""
给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。
如果目标值不存在于数组中，返回它将会被按顺序插入的位置。

你可以假设数组中无重复元素。
"""
from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # 36ms 91.22%
        for index, num in enumerate(nums):
            if num < target:
                continue
            elif num > target:
                nums.insert(index, target)
                return index
            elif num == target:
                return index
        else:
            # 位置在最尾部
            nums.append(target)
            return len(nums)-1



if __name__ == "__main__":
    test = [1,3,5,6]
    i = 5
    S = Solution()
    print(S.searchInsert(test, i))