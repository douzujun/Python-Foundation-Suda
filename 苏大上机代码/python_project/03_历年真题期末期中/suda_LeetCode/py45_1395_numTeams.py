# -*- coding: utf-8 -*-

class Solution:
    def numTeams(self, rating) -> int:
        rlen = len(rating)        
        res = 0
        for i in range(rlen-2):
            for j in range(i+1, rlen-1):
                for k in range(j+1, rlen):
                    if rating[i] > rating[j] > rating[k]:
                       res += 1
                    elif rating[i] < rating[j] < rating[k]:
                          res += 1

        return res
          
s = Solution()
print(s.numTeams(rating = [2,5,3,4,1]))
print(s.numTeams(rating = [2,1,3]))
print(s.numTeams(rating = [1,2,3,4]))
