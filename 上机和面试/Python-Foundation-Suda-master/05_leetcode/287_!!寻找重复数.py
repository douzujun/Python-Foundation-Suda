"""
给定一个包含 n + 1 个整数的数组 nums，
其数字都在 1 到 n 之间（包括 1 和 n），
可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/find-the-duplicate-number
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def findDuplicate(self, nums: list) -> int:
        for i in range(len(nums)-1):
            for j in range(len(nums)-1,i,-1):
                if nums[i] == nums[j]:
                    return nums[i]
        return 0

    def findDuplicate2(self, nums: list) -> int:
        # 二分法
        left, right = 1, len(nums)-1
        while left < right:
            mid = (left + right)//2
            count = 0
            for num in nums:
                # 统计小于mid的数字个数
                if num <= mid:
                    count += 1
            if count > mid:
                # 例如小于4的数字有4个
                right = mid
            else:
                left = mid + 1
        return left

    def findDuplicate3(self, nums:list) -> int:
        # 快慢指针
        slow=0
        fast=0
        while(1):
            slow=nums[slow]
            fast=nums[nums[fast]]
            if(slow==fast):
                break
        find=0
        while(1):
            # slow进入圈子兜兜转转
            find=nums[find]
            slow=nums[slow]
            if(find==slow):
                return find






if __name__ == "__main__":
    s1 = Solution()
    print(s1.findDuplicate3([1,3,4,2,2]))