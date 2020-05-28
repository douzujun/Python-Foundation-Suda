"""
非递减顺序数组A，返回每个数字的平方组成的新数组，也按非递减顺序排序
"""

class Solution:
    def sortedSquares(self, A:list) -> list:
        B = [pow(i,2) for i in A]
        B.sort()
        return B



if __name__ == "__main__":
    s1 = Solution()
    lst = list(map(int, input("请输入n个整数，用空格分开").split()))
    print(s1.sortedSquares(lst))