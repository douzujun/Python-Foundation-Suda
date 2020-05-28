# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 22:31:49 2020

@author: douzi
"""

class Solution:
    def shortestCompletingWord(self, licensePlate: str, words) -> str:
        import re
        awords = ''.join(re.findall('[a-zA-Z]+', licensePlate.lower()))
        
        words = sorted(words, key=lambda x:(len(x), words.index(x)))
        for word in words:
            for e in awords:
#                print(awords, word, e, awords.count(e), word.count(e))
                if e not in word or awords.count(e) > word.count(e):
                    break
            else:
                return word
    
    
s = Solution()
print(s.shortestCompletingWord(licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]))
print(s.shortestCompletingWord(licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]))
print(s.shortestCompletingWord("GrC8950", 
["measure","other","every","base","according","level","meeting","none","marriage","rest"]))
print(s.shortestCompletingWord("1s3 456", ["looks","pest","stew","show"]))