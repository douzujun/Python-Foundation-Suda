# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 00:03:29 2020

@author: douzi
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s == '':
            return 0
        if len(s) == 1:
            return 1
        
        def find_left(s, i):
            tmp_str = s[i]
            j = i - 1
            while j >= 0 and s[j] not in tmp_str:
                tmp_str += s[j]
                j -= 1
            return len(tmp_str)
        
        length = 0
        for i in range(0, len(s)):
            length = max(length, find_left(s, i))
        
        return length
    
s = Solution()
print(s.lengthOfLongestSubstring("pwwkew"))
print(s.lengthOfLongestSubstring("bbbbb"))
print(s.lengthOfLongestSubstring("abcabcbb"))

    