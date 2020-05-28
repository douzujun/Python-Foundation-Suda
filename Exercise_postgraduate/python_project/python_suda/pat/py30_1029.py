# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 21:52:11 2020

@author: douzi
"""

def solve():
    right = input().lower()
    wrong = input().lower()
    
    s1, s2 = set(right), set(wrong)
    out = list(s1 - s2)
    
    output = [[right.index(letter), letter] for letter in out]
    output.sort()
    
    olen = len(output)
    res = [str(output[i][1]) for i in range(olen)]
    
    print(''.join(res).upper())
    
solve()
                    
                    
        