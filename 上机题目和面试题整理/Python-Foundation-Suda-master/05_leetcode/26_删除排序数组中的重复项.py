"""
给定一个排序数组，你需要在 原地 删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。

不要使用额外的数组空间，你必须在 原地 修改输入数组 并在使用 O(1) 额外空间的条件下完成。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/remove-duplicates-from-sorted-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def removeDuplicates(self, nums: list) -> int:
        # 44ms 91.34%
        nums_set = set(nums)
        nums.clear()
        nums.extend(list(nums_set))
        nums.sort()
        return len(nums_set)
    
    def removeDuplicates2(self, nums):
        # 76ms 49%
        i = 0
        while i < len(nums):
            while i+1 < len(nums) and nums[i+1] == nums[i]:
                del nums[i+1]
            i += 1
        return len(nums)

    def removeDuplicates3(self, nums):
        # 60ms 66%
        # 倒着删除
        for i in range(len(nums))[::-1]:
            if i-1 != -1 and nums[i-1] == nums[i]:
                del nums[i] 
        return len(nums)




if __name__ == "__main__":
    nums = [0,0,1,1,1,2,2,3,3,4]
    s = Solution()
    print(s.removeDuplicates2(nums))
    print(nums)