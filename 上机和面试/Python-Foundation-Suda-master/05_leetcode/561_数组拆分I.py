"""
给定长度为 2n 的数组, 你的任务是将这些数分成 n 对,
例如 (a1, b1), (a2, b2), ..., (an, bn) ，
使得从1 到 n 的 min(ai, bi) 总和最大。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/array-partition-i
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def arrayPairSum(self, nums: list) -> int:
        # 376ms 43.66% 排序后求偶数位和
        nums.sort()
        return sum(nums[::2])

if __name__ == "__main__":
    test = [1,4,3,2]
    s = Solution()
    print(s.arrayPairSum(test))