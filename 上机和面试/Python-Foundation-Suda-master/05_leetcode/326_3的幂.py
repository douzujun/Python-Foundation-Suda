"""
给定一个整数，写一个函数来判断它是否是 3 的幂次方。

"""

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # 递归 76ms 98.96%
        return self.div3(n)

    def div3(self, n):
        if n == 1:
            return True
        elif n == 0:
            return False
        else:
            return n%3==0 and self.div3(n/3)

    def isPowerOfThree2(self, n):
        # 循环 96ms 61%
        while n not in (1, 0):
            n, m = divmod(n, 3)
            if m != 0:
                return False
        else:
            return True if n else False 
        

if __name__ == "__main__":
    S = Solution()
    print(S.isPowerOfThree2(9))