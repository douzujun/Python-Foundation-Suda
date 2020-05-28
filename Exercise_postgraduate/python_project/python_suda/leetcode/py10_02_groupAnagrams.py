# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 15:51:33 2020

@author: douzi
"""

class Solution:
    def groupAnagrams(self, strs):
        D = {}
        
        for w in strs:
            ks = tuple(sorted(w))
            if ks not in D:
                D[ks] = []
            D[ks].append(w)
 
        res = []
        for value in D.values():
            res.append(sorted(value))
        
        
        print(res)
        return res 
        
s = Solution()
s.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
            
        
        
        