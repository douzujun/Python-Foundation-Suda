# -*- coding: utf-8 -*-
class Solution:
    def romanToInt(self, s: str) -> int:
        dic = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    
        slen = len(s)
        ans = 0
        i = 0
        while i < slen:
            if i < slen - 1:
               if dic[s[i]] < dic[s[i+1]]:
                   ans += (dic[s[i+1]] - dic[s[i]])
                   i = i + 1
               else:
                   ans += dic[s[i]]
            else:
                ans += dic[s[i]]
            i = i + 1    
            
        return ans


s = Solution() 

print(s.romanToInt("III"))       
print(s.romanToInt('IV'))
print(s.romanToInt('IX'))
print(s.romanToInt('LVIII'))
print(s.romanToInt("MCMXCIV"))


