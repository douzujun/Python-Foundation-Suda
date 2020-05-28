# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 18:23:32 2020

@author: douzi
"""

def unit(n):
    res = ''
    for i in range(1, n+1):
        res += str(i)
    return res

def judge():
    n = int(input())
    
    hun = n // 100
    dec = n // 10 % 10
    un = n % 10
    
    res = hun*'B' + dec*'S' + unit(un)
    print(res)
    
judge()