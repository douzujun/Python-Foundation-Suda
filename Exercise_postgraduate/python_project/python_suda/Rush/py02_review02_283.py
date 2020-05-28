class Solution:
    def moveZeros(self, nums):
        for num in nums[::]:
            if num == 0:
                nums.remove(0)
                nums.append(0)
        return nums
        
s = Solution()
print(s.moveZeros([0, 1, 0, 3, 12]))