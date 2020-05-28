"""
输入n的值，求 
1/1 - 1/2 + 1/3 - 1/4 + 1/5 - 1/6 + 1/7 - 1/8 + ... + (-1)n-1·1/n 的值。
输入一个正整数n。1 <= n <= 1000。
返回一个字符串，该字符串的内容是一个保留小数点后四位整数的浮点数
"""

class Solution:
    def calc(self, n: int) -> str:
        res = 0
        for i in range(1, n+1, 2):
            res += 1/i
            res -= 1/(i+1)
        else:
            if n%2!=0:    # 奇数时补
                res += 1/(n+1)
        return ('%0.4f' % res)
        




if __name__ == "__main__":
    s1=Solution()
    num=int(input("请输入一个整数"))
    print(s1.calc(num))