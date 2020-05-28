"""
爱丽丝和鲍勃有不同大小的糖果棒：A[i] 是爱丽丝拥有的第 i 块糖的大小，B[j] 是鲍勃拥有的第 j 块糖的大小。

因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。
（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）

返回一个整数数组 ans，其中 ans[0] 是爱丽丝必须交换的糖果棒的大小，ans[1] 是 Bob 必须交换的糖果棒的大小。

如果有多个答案，你可以返回其中任何一个。保证答案存在。
"""

class Solution:
    def fairCandySwap(self, A: list, B: list) -> list:
        # 576ms 12.3%
        A_total, B_total = sum(A), sum(B)
        B_s = set(B)  # 转换成集合后会提升in的速度
        for a in A:
            b = a - (A_total - B_total) // 2
            if b in B_s:
                return [a, b]

    def fairCandySwap2(self, A: list, B: list) -> list:
        # 456ms 71.43
        Sa, Sb = sum(A), sum(B)
        setB = set(B)
        for x in A:
            if x + (Sb - Sa) // 2 in setB:
                return [x, x + (Sb - Sa) // 2]


if __name__ == "__main__":
    A = [1, 2, 5]
    B = [2, 4]
    s = Solution()
    print(s.fairCandySwap2(A, B))