"""
对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。
例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。

给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。

"""
from typing import List

class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        # 400ms 54.73%
        carry = 0
        index = len(A) - 1
        while K != 0:
            K, add = divmod(K, 10)
            if index >= 0:
                carry, add = divmod(add + carry + A[index], 10)
                A[index] = add
                index -= 1
            else:
                carry, add = divmod(add + carry, 10)
                A.insert(0, add)
        while carry:
            if index >= 0:
                carry, A[index] = divmod(carry + A[index], 10)
                index -= 1
            else:
                A.insert(0, carry)
                carry = 0
        return A

    def addToArrayForm2(self, A, K):
        # 344ms  80.56%  直接全部加在最低位 逐位取模
        A[-1] += K
        for i in range(len(A) - 1, -1, -1):
            carry, A[i] = divmod(A[i], 10)
            if i:
                # i 不等于0
                A[i-1] += carry
        if carry:
            A = list(map(int, str(carry))) + A
        return A

            
            


if __name__ == "__main__":
    # A, K = [1,2,0,0], 34
    # A, K = [0], 34
    # A, K = [7, 7], 34
    A, K = [9,9,9,9,9,9,9,9,9,9], 1
    S = Solution()
    print(S.addToArrayForm(A, K))