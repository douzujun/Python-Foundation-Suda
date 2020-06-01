# -*- coding: utf-8 -*-

class Solution:
    def shortestToChar(self, S: str, C: str):
        index = [i for i in range(len(S)) if S[i] is C]
        
        res = []
        slen = len(S)
        for i in range(slen):
            rmin = 100000
            for j in index:
                dis = abs(i - j)
                if rmin > dis:
                    rmin = dis
            res.append(rmin)                    
        
        print(res)
        return res
            
        
s = Solution()
print(s.shortestToChar(S = "loveleetcode", C = 'e'))