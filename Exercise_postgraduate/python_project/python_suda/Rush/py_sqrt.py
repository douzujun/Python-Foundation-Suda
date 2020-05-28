class Solution:
    def mySqrt(self, x: int) -> int:
        #return int(x**(1/2))
        low, high = 1, x
        while low <= high:
            mid = (low + high) // 2
            print(low, mid, high)
            if mid**2 == x:
                return mid
            elif mid**2 < x:
                low = mid + 1
            else:
                high = mid - 1
        return mid - 1

s = Solution()
print(s.mySqrt(8))
print(s.mySqrt(9))