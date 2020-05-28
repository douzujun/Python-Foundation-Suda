"""
给定一个二进制数组，计算其中最大连续1的个数
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: list) -> int:
        # 604ms 17.56%
        count, max_1 = 0, 0
        for num in nums:
            if num == 1:
                count += 1
            else:
                max_1 = max(count, max_1)
                count = 0
        return max(count, max_1)

    def findMaxConsecutiveOnes2(self, nums):
        # 532ms 30.57%
        zeros = [-1]
        zeros.extend([index for index,num in enumerate(nums) if num == 0])
        zeros.append(len(nums))
        return max([zeros[i+1] - zeros[i] -1 for i in range(len(zeros)-1)])

    def findMaxConsecutiveOnes3(self, nums):
        # map, join  684ms
        return max(map(len, ''.join(map(str,nums)).split('0')))


if __name__ == "__main__":
    s = Solution()
    print(s.findMaxConsecutiveOnes3([0]))