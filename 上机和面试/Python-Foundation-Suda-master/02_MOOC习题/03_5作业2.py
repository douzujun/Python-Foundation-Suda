"""
给定一个十进制正整数n，写下从1到n的所有整数，然后数一下其中出现的数字“1”的个数。

例如当n=2时，写下1,2。这样只出现了1个“1”；
当n=12时，写下1，2，3，4，5，6，7，8，9，10，11，12。这样出现了5个“1”。

正整数n。1 <= n <= 10000。
"""

class Solution:
    def count(self,n:int)->str:
        if not isinstance(n, int) or n>10000 or n <1:
            return
        res = 0
        for i in range(1, n+1):
            for ch in str(i):
                if ch == '1':
                    res += 1
            print(i, end=',')
        return res


if __name__ == "__main__":
    s1=Solution()
    num=int(input("请输入一个整数"))
    print(s1.count(num))