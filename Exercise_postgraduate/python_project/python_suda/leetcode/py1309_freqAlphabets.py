# -*- coding: utf-8 -*-

class Solution:
    def freqAlphabets(self, s: str) -> str:
        import string
        import re
        words = list(' ' + string.ascii_lowercase)

        li = s.split('#')
        
        res = ''                     # 结果
        wlen = len(li)
        for i in range(0, wlen- 1):
            w = li[i]                # '12345610'
            length = len(w)          
            if length <= 2:          
                w = int(w)
                res += str(words[w])
            else:
                front = w[:-2]
                beh = int(w[-2:])
                for e in front:
                    res += str(words[int(e)])
                res += str(words[int(beh)])
            
        end = li[-1]
        if end != '':
            for e in end:
                w = int(e)
                res += str(words[w])
        
        return res 
        
    
s = Solution()
s.freqAlphabets("10#11#12")
s.freqAlphabets("1326#")
s.freqAlphabets("25#")
        