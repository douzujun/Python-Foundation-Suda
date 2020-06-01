"""
给你一个非递减的 有序 整数数组，
已知这个数组中恰好有一个整数，
它的出现次数超过数组元素总数的 25%。
"""

class Solution:
    def findSpecialInteger(self, arr:list) -> int:
        target = len(arr) // 4 + 1
        i = 0
        count = 0
        while i < len(arr)-1:
            if arr[i] == arr[i+1]:
                count += 1
            else:
                count += 1
                if count >= target:
                    return arr[i]
                else:
                    count = 0
            i += 1
        else:
            return arr[i]

if __name__ == "__main__":
    arr = [1,2,2,6,6,6,6,7,10]
    s1 = Solution()
    print(s1.findSpecialInteger(arr))