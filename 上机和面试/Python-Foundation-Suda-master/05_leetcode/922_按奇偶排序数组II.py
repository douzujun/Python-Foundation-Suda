"""
给定一个非负整数数组 A， A 中一半整数是奇数，一半整数是偶数。

对数组进行排序，以便当 A[i] 为奇数时，i 也是奇数；当 A[i] 为偶数时， i 也是偶数。

你可以返回任何满足上述条件的数组作为答案。
905 I
"""

class Solution:
    def sortArrayByParityII(self, A: list) -> list:
        # 244 ms 71.34%  双指针
        odd, even = 0, 1   # 寻找错位奇数和错位偶数
        while odd < len(A):
            if A[odd] % 2 == 1:
                # 找到错位奇数
                if A[even] % 2 == 0:
                    # 找到错位偶数
                    A[odd], A[even] = A[even], A[odd]
                else:
                    even += 2
            else:
                odd += 2
        return A

    def sortArrayByParityII2(self, A):
        # 遍历两次A 236ms
        ans = [None] * len(A)
        ans[::2] = (x for x in A if x % 2 == 0)
        ans[1::2] = (x for x in A if x % 2 == 1)

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.sortArrayByParityII2([4, 2, 5, 7, 9, 9, 6, 6]))
