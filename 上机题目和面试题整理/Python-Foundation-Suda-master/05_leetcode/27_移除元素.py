"""
给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-element
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 32ms 92.97%  python特性解法
        for index in range(len(nums)-1,-1,-1):
            if nums[index] == val:
                del nums[index]
        return len(nums)

    def removeElement2(self, nums: List[int], val: int) -> int:
        # 题目想考察的  32ms 92.97%
        check, length = 0, -1
        while check < len(nums):
            if nums[check] == val:
                check += 1
            else:
                length += 1
                nums[length] = nums[check]
                check += 1
        return length+1


if __name__ == "__main__":
    S = Solution()
    nums = [0,1,2,2,3,0,4,2]
    val = 2
    length = S.removeElement2(nums, val)
    print(nums[:length])