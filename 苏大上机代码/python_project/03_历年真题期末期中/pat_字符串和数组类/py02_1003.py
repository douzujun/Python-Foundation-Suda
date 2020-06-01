# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 11:46:59 2020

@author: douzi
"""


import re

def judge():
    n = int(input())
    
    for i in range(n):
        s = input()
        if re.match(r'A*PA+TA*', s):
            a = re.split(r'[P|T]', s)
            if a[0]*len(a[1]) == a[2]:
                print("YES")
            else:
                print("NO")
        else:
            print("NO")
        
judge()