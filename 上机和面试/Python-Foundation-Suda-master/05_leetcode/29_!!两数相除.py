"""
给定两个整数，被除数 dividend 和除数 divisor。将两数相除，要求不使用  乘法、除法和 mod 运算符。

返回被除数 dividend 除以除数 divisor 得到的商。

整数除法的结果应当截去（truncate）其小数部分，例如：truncate(8.345) = 8 以及 truncate(-2.7335) = -2

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/divide-two-integers
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # 判断结果的符号
        neg = (dividend > 0) ^ (divisor > 0)    # 异或
        dividend = abs(dividend)
        divisor = abs(divisor)

        count = 0
        # 不断左移除数，直到其大于被除数
        while dividend >= divisor:
            count += 1
            divisor <<= 1
        result = 0
        while count > 0:
            count -= 1
            divisor >>= 1
            if divisor <= dividend:
                result += 1 << count    # 二进制(count+1位上的1)转换为十进制
                dividend -+ divisor
        # 符号
        if neg:
            result = -result
        # 判断溢出并返回
        return result if -(1<<31) <= result <= (1<<31)-1 else (1<<31)-1 

    def divide2(self, dividend: int, divisor: int) -> int:
        """
        a, b 除数被除数的绝对值
        r 倍数  t 当前除数为初始的多少倍
        """
        a, b, r, t = abs(dividend), abs(divisor), 0, 1
        while a >= b or t > 1:
            if a >= b: # 被除数大于除数
                r += t  
                a -= b
                t += t
                b += b
            else:      # 被除数小于除数  除数转为原来的一半
                t >>= 1     # 二进制移位相当于//2
                b >>= 1
        return min((-r, r)[dividend ^ divisor >= 0], (1 << 31) - 1)

if __name__ == "__main__":
    s = Solution()
    print(s.divide2(-2147483648, -1))