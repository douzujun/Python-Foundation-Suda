"""
给定一个正整数 num，编写一个函数，如果 num 是一个完全平方数，则返回 True，否则返回 False。

说明：不要使用任何内置的库函数，如  sqrt。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-perfect-square
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # 36ms 80%
        if (num ** (1/2)).is_integer():
            return True
        else:
            return False

    def isPerfectSquare2(self, num):
        # 52ms 27%
        i = 1
        while i*i<num:
            i += 1
        return i * i == num

    def isPerfectSquare3(self, num):
        # 40ms 63.94%
        # 等差数列法  完全平方数可以表示为 1 ~ (2N-1)的奇数和
        i = 1
        while num > 0:
            num -= i
            i += 2
        return num == 0


if __name__ == "__main__":
    S = Solution()
    test = 16
    print(S.isPerfectSquare(test))
