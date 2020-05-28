"""
给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：

A.length >= 3
在 0 < i < A.length - 1 条件下，存在 i 使得：
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/valid-mountain-array
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。
"""

class Solution:
    def validMountainArray(self, A: list) -> bool:
        if len(A) < 3:
            return False
        prvious = A[0]
        for i in range(1, len(A)):
            if A[i] == prvious:
                return False
            elif A[i] > prvious:
                prvious = A[i]
            else:
                break
        
        if i == len(A) or i == 1:
            # 只有一半山脉
            return False
        
        for j in range(i, len(A)):
            if A[j] == prvious:
                return False
            elif A[j] < prvious:
                prvious = A[j]
            else:
                prvious = A[j]
                return False
        return True

if __name__ == "__main__":
    s1 = Solution()
    # print(s1.validMountainArray([2,1]))
    # print(s1.validMountainArray([3,5,5]))
    # print(s1.validMountainArray([0,3,2,1]))
    
    print(s1.validMountainArray([9,8,7,6,5,4,3,2,1,0]))
