"""
斐波那契数，通常用 F(n) 表示，形成的序列称为斐波那契数列。

该数列由 0 和 1 开始，后面的每一项数字都是前面两项数字的和。也就是：

F(0) = 0,   F(1) = 1
F(N) = F(N - 1) + F(N - 2), 其中 N > 1.

给定 N，计算 F(N)。
"""

class Solution:
    def fib(self, N: int) -> int:
        # "移步法"
        N_f, N_r = 1, 0
        if N == 0:
            return N_r
        elif N == 1:
            return N_f
        else:
            n = 1
            while n < N:
                N_f, N_r = (N_f + N_r), N_f
                n += 1
            return N_f


if __name__ == "__main__":
    s = Solution()
    print(s.fib(4))