"""
给定一个数组nums，
编写一个函数将所有0移动到数组的末尾，
同时保持非零元素的相对顺序
"""
class Solution:
    def moveZeroes(self, nums: list) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1:
            # nums有0或1个元素 或 没有0元素 返回
            return None

        count_zeros, index = 0, 0
        while index < len(nums):
            # 数0的个数并删除中间出现的0
            if nums[index] == 0:
                del nums[index]
                count_zeros += 1
            else:
                index += 1
        
        for _ in range(count_zeros):
            nums.append(0)
            

if __name__ == "__main__":
    nums = [0,1,0,3,12]
    # nums = [1]
    print(nums)
    s = Solution()
    s.moveZeroes(nums)
    print(nums)