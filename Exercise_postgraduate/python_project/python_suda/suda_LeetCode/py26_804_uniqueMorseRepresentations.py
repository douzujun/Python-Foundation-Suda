# -*- coding: utf-8 -*-

class Solution:
    def uniqueMorseRepresentations(self, words) -> int:
        import string
        letters = string.ascii_lowercase
        table = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        wlen = len(words)
        T = []
        for i in range(wlen):
            str2 = ''
            wl = len(words[i])
            for j in range(wl):
                k = letters.index(words[i][j])
                str2 += table[k]
            if str2 not in T:
                T.append(str2)
        
        print(T)
        return len(T)
    
s = Solution()
print(s.uniqueMorseRepresentations(words = ["gin", "zen", "gig", "msg"]))

