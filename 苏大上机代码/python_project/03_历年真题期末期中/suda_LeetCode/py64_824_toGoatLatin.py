# -*- coding: utf-8 -*-

class Solution:
    def toGoatLatin(self, S: str) -> str:
        res = []
        S = S.split()
        cnt = 1
        for e in S:
            if e[0].lower() in ['a','e','i', 'o', 'u']:
                res.append(e + 'ma' + cnt*'a')
            else:
                res.append(e[1:] + e[0] + 'ma' + cnt*'a')
            cnt = cnt + 1
        return ' '.join(res)
    
s = Solution()
print(s.toGoatLatin("I speak Goat Latin"))
print(s.toGoatLatin("The quick brown fox jumped over the lazy dog"))
