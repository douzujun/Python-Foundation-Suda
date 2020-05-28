"""
给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

说明：你不能倾斜容器，且 n 的值至少为 2。

图中垂直线代表输入数组 [1,8,6,2,5,4,8,3,7]。在此情况下，容器能够容纳水（表示为蓝色部分）的最大值为 49。
"""

class Solution:
    def maxArea(self, height: list) -> int:
        # 超时 N^2  暴力
        maxA = 0
        for i in range(len(height)-1):
            for j in range(i + 1, len(height)):
                tempA = (j-i) * min(height[i], height[j])
                maxA = max(tempA, maxA)
        return maxA

    def maxArea2(self, height):
        # 72ms  74.45%
        # 双指针  每次移动小的一边（无论怎么移动大的容量都不会变大 缩减问题边界）
        left, right = 0, len(height) - 1
        ans = 0
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            ans = max(ans, area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return ans

if __name__ == "__main__":
    S = Solution()
    print(S.maxArea([1,8,6,2,5,4,8,3,7]))