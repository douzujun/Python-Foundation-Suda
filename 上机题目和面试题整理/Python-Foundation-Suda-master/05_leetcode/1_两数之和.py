"""
给定一个整数数组 nums 和一个目标值 target，
请你在该数组中找出和为 目标值 的那 两个 整数，并返回他们的数组 下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。
"""


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        for index, num in enumerate(nums):
            temp = target - num
            try:
                index2 = nums.index(temp)
            except:
                continue
            if index == index2:
                continue
            return [index, index2]

    def twoSum2(self, nums: list, target: int) -> list:
        num_dict = {}
        for index, num in enumerate(nums):
            temp = target - num
            if temp in num_dict:
                return num_dict[temp], index
            else:
                num_dict[num] = index
            

if __name__ == "__main__":
    s = Solution()
    nums = [2, 7, 11, 15]
    target = 9
    print(s.twoSum(nums, target))
    