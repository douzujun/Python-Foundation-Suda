"""
给定一个正整数，返回它在 Excel 表中相对应的列名称。
    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB 

15:17 -> 
"""

class Solution:
    def convertToTitle(self, n: int) -> str:
        # 32ms 89.07% 辗转相除法 26进制
        start = ord('A')
        ans = []
        while n > 0:
            n -= 1      # 关键
            n, t = divmod(n, 26)
            ans.append(chr(start + t))

        return ''.join(ans[::-1])


if __name__ == "__main__":
    S = Solution()
    print(S.convertToTitle(27))
    # print(S.convertToTitle(701))
    # print(S.convertToTitle(52))