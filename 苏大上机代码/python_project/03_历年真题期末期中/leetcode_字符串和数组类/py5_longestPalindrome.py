# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 18:03:04 2020

@author: douzi
"""

class Solution:
    def longestPalindrome(self, s: str) -> str:
        length = len(s)
        result = ""
        for i in range(length):
            sum1 = ""
            sum2 = ""
            for str1 in s[i:]:
                sum1 = sum1 + str1
                sum2 = str1 + sum2
                if sum1 == sum2 and len(sum1) > len(result):
                    result = sum1
                else:
                    continue
        return result
    
s = Solution()
print(s.longestPalindrome('babad'))
print(s.longestPalindrome('cbbd'))
