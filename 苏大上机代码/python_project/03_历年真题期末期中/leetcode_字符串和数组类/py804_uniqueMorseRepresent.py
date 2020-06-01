# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 23:38:05 2020

@author: douzi
"""

class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        import string
        letters = list(string.ascii_lowercase)
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        wlen = len(words)
        T = []
        for i in range(wlen):
            str2 = ''
            wl = len(words[i])         # 求单词的编码
            for j in range(wl):
                k = letters.index(words[i][j])
                str2 += table[k]
            if str2 not in T:
                T.append(str2)
        
        return len(T)
                
s = Solution()
print(s.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]))

