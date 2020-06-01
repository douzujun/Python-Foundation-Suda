# -*- coding: utf-8 -*-

class Solution:
    def removePalindromeSub(self, s: str) -> int:
        
        def isPalid(word):
            wlen = len(word)
            for i in range(wlen):
                if word[i] != word[wlen - i - 1]:
                    return False
            return True
        
        sli = s[::]
        res = 0
        for e in sli:
            if isPalid(s):
                res += 1
                return res
            else:
                res += 1
                s = s.replace(e, '') 
                
        return 0

    
s = Solution()
print(s.removePalindromeSub('ababa'))
print(s.removePalindromeSub('abb'))   
print(s.removePalindromeSub('baabb')) 
print(s.removePalindromeSub(''))
            