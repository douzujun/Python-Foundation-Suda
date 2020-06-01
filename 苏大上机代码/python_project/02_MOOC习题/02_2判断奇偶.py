"""
给定一个整数num,判断其是奇数还是偶数，返回值为字符串

如果num是奇数, 返回"odd";

如果num是偶数, 返回"even";
"""


class Solution:
    def judge(self,  num: int) -> str:
        if num % 2 ==0:
            return "even"
        else:
            return "odd"


if __name__ == "__main__":
    s1 = Solution()
    while True:
        try:
            num = int(input("请输入一个整数"))
            print(s1.judge(num))
        except:
            break
