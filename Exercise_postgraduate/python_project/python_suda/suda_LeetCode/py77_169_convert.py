# -*- coding: utf-8 -*-

class Solution:
    def convertToTitle(self, n: int) -> str:
       
        dic = {}
        for i in range(0, 25):
            dic[i+1] = chr(ord('A')+i)
        dic[0] = 'Z'
            
        res = ''
        while n > 0:
            res += dic[n % 26]
            if n % 26 != 0:
                n = n // 26
            else:
                n = (n - 26) // 26
        
        return res[::-1]
    
s = Solution()
print(s.convertToTitle(1))
print(s.convertToTitle(28))
print(s.convertToTitle(27))
print(s.convertToTitle(701))
print(s.convertToTitle(52))
        
        