"""
自除数 是指可以被它包含的每一位数除尽的数。

例如，128 是一个自除数，
因为 128 % 1 == 0，128 % 2 == 0，128 % 8 == 0。

还有，自除数不允许包含 0 。

给定上边界和下边界数字，输出一个列表，
列表的元素是边界（含边界）内所有的自除数。

示例 1：

输入： 

上边界left = 1, 下边界right = 22

输出： [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 12, 15, 22]
"""

class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list:
        result = []
        for num in range(left, right+1):
            num_copy = num
            while num_copy != 0:
                temp = num_copy % 10
                if temp == 0:
                    break
                elif num % temp !=0:
                    break
                num_copy //= 10
            else:
                result.append(num)
        return result



if __name__ == "__main__":
    s1=Solution()
    left=int(input("请输入一个整数上边界"))
    right=int(input("请输入一个整数下边界"))
    print(s1.selfDividingNumbers(left,right))