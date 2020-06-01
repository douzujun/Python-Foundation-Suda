"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。
请根据这个假设，如果反转后整数溢出那么就返回 0。
"""
class Solution:
    def reverse(self, x: int) -> int:
        # 52ms 字符串
        if x > 0:
            x_str = str(x)
        else:
            x_str = str(-x) + '-'
        ans = int(''.join(reversed(x_str)))

        if ans >= 2147483647 or ans <= -2147483648:
        # if ans >= (1 << 31) -1 or ans <= -1<<31:
            return 0
        else:
            return ans

    def reverse2(self, x):
        # 36ms 83.22%
        y, res = abs(x), 0
        # 则其数值范围为 [−2^31,  2^31 − 1] 根据正负来选择边界
        boundry = (1<<31) -1 if x > 0 else 1 << 31
        while y != 0:
            # 结果*10 加上y的末尾
            res = res*10 + y%10
            if res > boundry :
                return 0
            y //=10
        return res if x >0 else -res


if __name__ == "__main__":
    s = Solution()
    print(s.reverse(1534236469))
    print(s.reverse2(-2147483412))

