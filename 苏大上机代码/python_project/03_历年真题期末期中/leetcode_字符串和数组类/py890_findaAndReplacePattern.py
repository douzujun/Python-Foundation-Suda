# -*- coding: utf-8 -*-
"""
Created on Sat Mar 28 22:03:28 2020

@author: douzi
"""
#    输入：words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
#    输出：["mee","aqq"]
#    解释：
#    "mee" 与模式匹配，因为存在排列 {a -> m, b -> e, ...}。
#    "ccc" 与模式不匹配，因为 {a -> c, b -> c, ...} 不是排列。
#    因为 a 和 b 映射到同一个字母。
class Solution:
    def findAndReplacePattern(self, words, pattern: str):
        # 是否有模式匹配
        def check(word, pattern): 
            if len(word) != len(pattern):
                return False
            for i in range(len(word)):
                if word.index(word[i]) != pattern.index(pattern[i]):
                    return False
            return True
        
        res = []
        for word in words:
             if check(word, pattern):
               res.append(word)
               
#        print(res)
        return res
        
    
    
s = Solution()
s.findAndReplacePattern(["abc","deq","mee","aqq","dkd","ccc"], "abb")