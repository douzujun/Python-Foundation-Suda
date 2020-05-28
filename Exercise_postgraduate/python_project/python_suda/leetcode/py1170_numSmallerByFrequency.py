# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 15:24:05 2020

@author: douzi
"""

class Solution:
    def numSmallerByFrequency(self, queries, words):
        def check(s):
            return s.count(min(s))
        
        res = []
        # 先存储一遍words中的最小值，以免重复计算
        words_cnt = [check(word) for word in words]
        for item in queries:
            # 避免重复计算
            f_item = check(item) 
            res.append(len([1 for cnt in words_cnt if f_item < cnt]))
        
#        print(res)
        return res
        
        
s = Solution()
s.numSmallerByFrequency(queries = ["cbd"], words = ["zaaaz"])

s.numSmallerByFrequency(queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"])          

s.numSmallerByFrequency(["bba","abaaaaaa","aaaaaa","bbabbabaab","aba","aa","baab","bbbbbb","aab","bbabbaabb"],
["aaabbb","aab","babbab","babbbb","b","bbbbbbbbab","a","bbbbbbbbbb","baaabbaab","aa"])