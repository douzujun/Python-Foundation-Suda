# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 16:40:47 2020

@author: douzi
"""
#[('c', 1), ('b', 1), ('a', 1), ('f', 1), ('g', 1)]
#[('a', 1), ('b', 2), ('c', 1), ('d', 1)]
#['c', 'b', 'a', 'd']
#['c', 'b', 'b', 'a', 'd']
#cbbad
#{'c': 1, 'b': 2, 'a': 1, 'f': 0, 'g': 0}
#dcbba


class Solution:
    def customSortString(self, S: str, T: str) -> str:
        import collections
        cs = collections.Counter(S)
        print(list(cs.items()))
        ct = collections.Counter(T)
        print(list(ct.items()))
        
        print(list((cs + ct - cs)))
        print(list((cs + ct - cs).elements()))
        
        # cs + ct - cs  
        return ''.join(list((cs + ct - cs).elements()))
    
    def customSortString2(self, S, T):
        d = {c:0 for c in S}
        
        ans = ''
        for c in T:
            if c in d:
                d[c] += 1
            else:
                ans += c       #   
            
        print(d)
        for c in d:
            ans += c * d[c]
            
        return ans
            
    
s = Solution()
#print(s.customSortString('cbafg', 'abcdb'))
print(s.customSortString2('cbafg', 'abcdb'))



























