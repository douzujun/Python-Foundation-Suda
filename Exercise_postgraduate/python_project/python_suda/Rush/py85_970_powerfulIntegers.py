from typing import List

class Solution:
    def powerfulIntegers(self, x: int, y: int, bound: int) -> List[int]:
        from math import log
        ans = set()
        
        i_max = int(log(bound, x))+1 if x > 1 else 1
        j_max = int(log(bound, y))+1 if y > 1 else 1
        for i in range(i_max):
            for j in range(j_max):
                comb = x**i + y**j
                if comb <= bound:
                    ans.add(comb)
        
        return list(ans)

s = Solution()

print(s.powerfulIntegers(x = 2, y = 3, bound = 10))
print(s.powerfulIntegers(x = 3, y = 5, bound = 15))
print(s.powerfulIntegers(2, 1, 10))
print(s.powerfulIntegers(1, 2, 100))