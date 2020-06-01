# -*- coding: utf-8 -*-
class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
#        xbin = bin(x)[2:]
#        ybin = bin(y)[2:]
#        
#        print(xbin, ybin)
#        bmax = len(xbin) if len(xbin) > len(ybin) else len(ybin)
#        
#        res = 0
#        xbin = ('{0:0'+str(1+bmax)+'d}').format(int(xbin))
#        ybin = ('{0:0'+str(1+bmax)+'d}').format(int(ybin))
#                
#        maxb = len(xbin)
#        for i in range(maxb):
#            if xbin[i] != ybin[i]:
#                res += 1
#        
#        print(res)
#        return res
        return bin(x ^ y).count('1')
    
    
s = Solution()
print(s.hammingDistance(x=1, y=4))


        