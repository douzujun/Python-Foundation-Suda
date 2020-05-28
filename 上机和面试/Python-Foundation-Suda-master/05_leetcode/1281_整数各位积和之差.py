"""
给你一个整数 n，
请你帮忙计算并返回该整数「各位数字之积」与「各位数字之和」的差。
"""

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        Sum, Product = 0, 1
        while n > 0:
            n, m = divmod(n, 10)
            Sum += m
            Product *= m
        return Product - Sum

    def subtractProductAndSum2(self, n):
        from functools import reduce #used in python3
        num=list(map(int, list(str(n))))
        return reduce(lambda x,y:x*y,num)-sum(num)



if __name__ == "__main__":
    s1 = Solution()
    while True:
        try:
            n = int(input())
            print(s1.subtractProductAndSum(n))
        except:
            break
