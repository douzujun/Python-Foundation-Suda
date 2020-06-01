# -*- coding: utf-8 -*-
"""
Created on Thu Apr  2 00:44:00 2020

@author: douzi
"""
# 输入：s = "TO BE OR NOT TO BE"
# 输出：["TBONTB","OEROOE","   T"]
# 解释：题目允许使用空格补位，但不允许输出末尾出现空格。
# "TBONTB"
# "OEROOE"
# "   T"
class Solution:
    def printVertically(self, s: str):
        s = s.split(' ')
        max_1 = 0
        for w in s:
            max_1 = max(max_1, len(w))
        
        r = [[] for i in range(max_1)]
        
        for w in s:
            for i in range(max_1):
                if i < len(w):
                    # 第i个列表，存放word的第i个单词 
                    r[i].append(w[i])
                else:
                    r[i].append(' ') 
        
        res = []
        print(r)
        # 去除末尾空格 
        for x in r:
            res.append(''.join(x).rstrip())
        
        return res
    
s = Solution()
print(s.printVertically(s = "TO BE OR NOT TO BE"))
        
        