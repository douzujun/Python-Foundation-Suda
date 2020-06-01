# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 20:34:37 2020

@author: douzi
"""

def solve():
    data = input()
    dlen = len(data)
    
    res = ''
    pattern = 'PATest'
    for i in range(dlen):
        for m in pattern:
            if data.find(m) != -1:
                data = data.replace(m, '', 1)
                res += m
          
    print(res)
    
solve()
        
        