# -*- coding: utf-8 -*-
"""
Created on Fri Mar 27 17:05:47 2020

@author: douzi
"""

class Solution:
    def sortString(self, s: str) -> str:
        if not s:
            return ''
        
        s = list(s)
        res = []
        while s:               # len(s) 次循环
            c_list = list(set(s))
            c_list.sort()               # 升序
            for i in c_list:
                res.append(i)
                s.remove(i)             # 从原来字符里删除
                
            c_list = list(set(s))
            c_list.sort(reverse=True)   # 倒序
            for i in c_list:
                res.append(i)
                s.remove(i)
                
        return ''.join(res)
                
        
    
s = Solution()
print(s.sortString("aaaabbbbcccc"))
print(s.sortString("rat"))
print(s.sortString("leetcode"))
print(s.sortString("ggggggg"))
