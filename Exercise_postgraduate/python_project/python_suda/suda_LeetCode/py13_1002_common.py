# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 01:37:11 2020

@author: douzi
"""

class Solution:
    def commonChars(self, A):
        res = list()
        
        for w in set(A[0]):     # 遍历每个字符
            cnt = [x.count(w) for x in A]   # 每个单词的 字符w 数量
            a = w * min(cnt)
            for i in a:               # 防止不是全部都出现的，且分开添加
                res.append(i)
             
        return res
        
s = Solution()
print(s.commonChars(["bella","label","roller"]))

print(s.commonChars(["cool","lock","cook"]))