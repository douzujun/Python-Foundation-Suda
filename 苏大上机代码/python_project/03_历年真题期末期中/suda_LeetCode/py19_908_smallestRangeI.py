# -*- coding: utf-8 -*-

class Solution:
    def smallestRangeI(self, A, K: int) -> int:
#       数组中最小值和最大值相差大于两倍的K时，最小差值为最大值和最小值之差减两倍的K；
#       当最小值和最大值相差小于或等于两倍的K时，最小差值为0。
        return max(max(A) - min(A) - 2*K, 0)

    
s = Solution()
print(s.smallestRangeI(A = [1], K = 0))

print(s.smallestRangeI(A = [0,10], K = 2))

print(s.smallestRangeI(A = [1,3,6], K = 3))
        