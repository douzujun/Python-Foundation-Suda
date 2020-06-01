# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:11:09 2020

@author: douzi
"""

def solve():
    A = input()
    B = input()
    
    data = A + B
    
    res = ''
    for e in data:
        if e not in res:
            res += e
    
    print(res)
    
    
solve()