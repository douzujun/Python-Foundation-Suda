"""
编写一个程序判断给定的数是否为丑数。

丑数就是只包含质因数 2, 3, 5 的正整数。
"""


class Solution:
    def isUgly(self, num: int) -> bool:
        # 44ms 51%
        if num <= 0:
            return False
        while num % 2 == 0:
            num = num // 2
        while num % 3 == 0:
            num = num // 3
        while num % 5 == 0:
            num = num // 5
        if num != 1:
            return False
        else:
            return True
    
    def isUgly2(self, num: int) -> bool:
        # 44ms
        if num <= 0:
            return False
        
        x = (2,3,5)
        while num!=1:
            for i in x:
                if num%i == 0:
                    num //= i
                    break
            else:
                return False
        return True
        
    def isUgly3(self, num):
        # 40ms
        if num <= 0:  ## 如果num非正，就不是丑数
            return False
        while True:
            last = num
            if not num % 2:  ## 如果2整除num，就除以2
                num >>= 1
            if not num % 3:  ## 如果3整除num，就除以3
                num //= 3
            if not num % 5:  ## 如果5整除num，就除以5
                num //= 5
            if num == 1:  ## 如果若干次操作后，num变成1，说明num的因数只有2、3、5，是丑数
                return True
            if last == num:  ## 如果1轮操作后，num没变，说明num不是丑数
                return False



if __name__ == "__main__":
    s = Solution()
    print(s.isUgly(14))

