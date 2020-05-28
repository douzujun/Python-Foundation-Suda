# -*- coding: utf-8 -*-

class Solution:
    def numRabbits(self, answers) -> int:
        if not answers:
            return 0
        
        d = {}
        for cnt in answers:
            d[cnt] = d.get(cnt, 0) + 1
        
        ans = 0
        for key, value in d.items():
            if key == 0:
                ans += value
            else:
                cnt = key + 1
                ans += ((value + cnt - 1) // cnt) * cnt
        
        return ans
    
s = Solution()

print(s.numRabbits(answers = [1, 1, 2]))
print(s.numRabbits(answers = [10, 10, 10]))
print(s.numRabbits(answers = []))
        
