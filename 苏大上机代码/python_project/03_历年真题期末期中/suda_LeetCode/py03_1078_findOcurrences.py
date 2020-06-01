# -*- coding: utf-8 -*-

class Solution:
    def findOcurrences(self, text: str, first: str, second: str): #-> List[str]:
        words = text.split(' ')
        res = []
        
        wlen = len(words)
        for i in range(0, wlen - 2):
            if words[i] == first and words[i + 1] == second:
                res.append(words[i + 2])
            
        return res
    
    
s = Solution()
print(s.findOcurrences(text = "alice is a good girl she is a good student", first = "a", second = "good"))
print(s.findOcurrences(text = "we will we will rock you", first = "we", second = "will"))


        
        
        