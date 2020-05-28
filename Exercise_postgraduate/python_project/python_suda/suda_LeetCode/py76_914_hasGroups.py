# -*- coding: utf-8 -*-

class Solution:
    def hasGroupsSizeX(self, deck) -> bool:
        import math
        dlen = len(deck)        
        if dlen < 2:
            return False

        cnt = [deck.count(e) for e in deck]

        mygcd = 9999999
        for i in range(dlen - 1):
            t = math.gcd(cnt[i], cnt[i + 1])
            if mygcd > t:
                mygcd = t
        
        if mygcd == 1:
            return False
        
        for i in range(dlen - 1):
            if cnt[i] % mygcd != 0:
                return False
        return True
    
s = Solution()
print(s.hasGroupsSizeX([1,2,3,4,4,3,2,1]))
print(s.hasGroupsSizeX([1]))
print(s.hasGroupsSizeX([1,1,2,2,2,2]))
print(s.hasGroupsSizeX([1,1,1,1,2,2,2,2,2,2]))
        