"""
给你一个整数数组 A，对于每个整数 A[i]，
我们可以选择处于区间 [-K, K] 中的任意数 x ，
将 x 与 A[i] 相加，结果存入 A[i] 。

在此过程之后，我们得到一些数组 B。
返回 B 的最大值和 B 的最小值之间可能存在的最小差值。
"""
class Solution:
    def smallestRangeI(self, A: list, K: int) -> int:
        # 152 ms  44%
        m, n = max(A), min(A)
        return max(m - n - 2*K, 0)

    def smallestRangeI2(self, A: list, K: int) -> int:
        # 132 ms  87%
        m, n = 0, 10000
        for num in A:
            if num > m:
                m = num
            if num < n:
                n = num
        return max(m - n - 2*K, 0)


if __name__ == "__main__":
    A, k = [1, 3, 6], 3
    S = Solution()
    print(S.smallestRangeI2(A, k))