# -*- coding: utf-8 -*-

class Solution:
    def wordPattern(self, pattern: str, str1: str) -> bool:
        pli = list(pattern)
        sli = str1.split()
        plen = len(pli)
        slen = len(sli)
        if plen != slen:
            return False
        for i in range(slen):
            if pli.index(pli[i]) != sli.index(sli[i]):
                return False
        return True
    
s = Solution()
print(s.wordPattern("abba", "dog cat cat dog"))
print(s.wordPattern("aaa", "aa aa aa aa"))