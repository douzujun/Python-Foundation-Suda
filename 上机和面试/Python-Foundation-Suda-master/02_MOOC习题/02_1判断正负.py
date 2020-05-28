"""
给定一个整数num,判断其正负，返回值为字符串。

如果num, > 0, 返回"positive";

如果num, = 0, 返回"zero";

如果num, < 0, 返回"negative"
"""


class Solution:
    def judge(self, num: int) -> str:
        if num > 0:
            return "positive"
        elif num < 0:
            return "negative"
        else:
            return "zero"



if __name__ == "__main__":
    s1 = Solution()
    while True:
        try:
            num = int(input("请输入一个整数"))
            print(s1.judge(num))
        except:
            break
