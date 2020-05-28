"""
给定一个非负整数数组 A，返回一个数组，在该数组中， 
A 的所有偶数元素之后跟着所有奇数元素。

你可以返回满足此条件的任何数组作为答案。
922 II
"""

class Solution:
    def sortArrayByParity(self, A: list) -> list:
        # 88ms 82% 双指针 交换奇数到尾部
        front, rear = 0, len(A)-1
        while front < rear:
            if A[front] % 2 == 0:
                # 偶数
                front += 1
            else:
                A[front], A[rear] = A[rear], A[front]
                rear -= 1
        return A

    def sortArrayByParity2(self, A:list) -> list:
        # 92ms
        front, rear = 0, len(A) - 1
        while True:
            while front < len(A) and A[front] % 2 == 0:
                # 找奇数
                front += 1
            while 0 < rear and A[rear] % 2 == 1:
                # 找偶数
                rear -= 1
            if front < rear:
                A[front], A[rear] = A[rear], A[front]
            else:
                break

        return A


if __name__ == "__main__":
    test = [3,1,2,4]
    s = Solution()
    print(s.sortArrayByParity2(test))
