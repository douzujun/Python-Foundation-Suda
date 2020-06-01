# -*- coding: utf-8 -*-

class Solution:
    def findComplement(self, num: int) -> int:
        nbin = bin(num)
        print(nbin)
        
        comp = '0b'
        for e in nbin[2:]:
            if e == '0':
                comp += '1'
            else:
                comp += '0'

        return int(comp, 2)

s = Solution()
print(s.findComplement(5))

print(s.findComplement(1))