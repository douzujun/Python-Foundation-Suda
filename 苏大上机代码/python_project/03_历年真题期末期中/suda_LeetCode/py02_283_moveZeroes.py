class Solution:
    def moveZeroes(self, nums) -> None:
        for e in nums[::]:
            if e == 0:
                nums.remove(e)
                nums.append(0)
    
        return nums
            

s = Solution()
print(s.moveZeroes([0, 1, 0, 3, 12]))
