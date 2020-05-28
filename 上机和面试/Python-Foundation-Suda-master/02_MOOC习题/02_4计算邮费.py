"""
根据邮件的重量和用户是否选择加急计算邮费。
计算规则：重量在1000克以内(包括1000克), 基本费8元。
超过1000克的部分，每500克加收超重费4元，不足500克部分按500克计算；
如果用户选择加急，多收5元。

输入：重量一定是整数，是否加急是一个字符，如果是大写或者小写Y表示加急，否则是不加急。
"""


class Solution:
    def calc(self,  num: int, flag: str) -> int:
        total = 8
        if flag == "Y" or flag == "y":
            total += 5
        if num > 1000:
            num -= 1000
            r = num // 500
            if num % 500 != 0:
                r += 1
            total += r*4
        return total

if __name__ == "__main__":
    s1 = Solution()
    while True:
        try:
            num = int(input("请输入重量"))
            flag = input("请输入是否加急(Y/N)")
            print(s1.calc(num, flag))
        except:
            break
