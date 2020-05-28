# -*- coding: utf-8 -*-

class Solution:
    def flipAndInvertImage(self, A):
        res = []
        for li in A:
            li.reverse()
            rlen = len(li)
            for i in range(rlen):
                if li[i] == 0:
                    li[i] = 1
                else:
                    li[i] = 0
            res.append(li)
        
        return res
    
    
s = Solution()
print(s.flipAndInvertImage([[1,1,0],[1,0,1],[0,0,0]]))

print(s.flipAndInvertImage([[1,1,0,0],[1,0,0,1],[0,1,1,1],[1,0,1,0]]))


        
        
