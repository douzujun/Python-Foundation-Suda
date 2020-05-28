"""
在大小为 2N 的数组 A 中有 N+1 个不同的元素，其中有一个元素重复了 N 次。

返回重复了 N 次的那个元素。
"""

class Solution:
    def repeatedNTimes(self, A) -> int:
        from random import randint
        while True:
            i = randint(0, len(A)-1)
            j = randint(0, len(A)-1)
            if i != j and A[i] == A[j]:
                return A[i]
