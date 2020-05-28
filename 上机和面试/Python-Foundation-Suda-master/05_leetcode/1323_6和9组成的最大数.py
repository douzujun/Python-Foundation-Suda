"""
给你一个仅由数字 6 和 9 组成的正整数 num。

你最多只能翻转一位数字，将 6 变成 9，或者把 9 变成 6 。

请返回你可以得到的最大数字。
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        num_list = list(str(num))
        for index, num in enumerate(num_list):
            if num == '6':
                num_list[index] = '9'
                break

        return int(''.join(num_list))

    def maximum69Number2(self, num:int):
        # 替换次数
        return int(str(num).replace('6', '9', 1))


if __name__ == '__main__':
    s1 = Solution()
    print(s1.maximum69Number(6669))