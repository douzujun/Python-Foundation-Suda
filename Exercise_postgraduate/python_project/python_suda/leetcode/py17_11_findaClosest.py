# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 20:20:19 2020

@author: douzi
"""

class Solution:
    def findClosest(self, words, word1: str, word2: str) -> int:
        
        res = 1000000
        i = 0
        wlen = len(words)
        while i < wlen:
            if word1 == words[i]:
                for j in range(0, wlen):
                    if word2 == words[j]:
                        dis = abs(i - j)
                        if res > dis:
                            res = dis
            i = i + 1
        
        return res
    
s = Solution()
s.findClosest(["I","am","a","student","from","a","university","in","a","city"], 'a', 'student')
        