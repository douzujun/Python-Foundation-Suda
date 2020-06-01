# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:49:20 2020

@author: douzi
"""

import re

def fun6():
    S = input('输入单词S:')
    T = input("输入单词T:")
    sli = re.findall('[a-z]', S)
    slist = list(set(sli))
    tli = re.findall('[a-z]', T)
    tlist = list(set(tli))
    
    a = 0
    slen = len(slist)
    tlen = len(tlist)
    for i in range(slen):
        for j in range(i, tlen):
            if slist[i] == tlist[j]:
                a = a + 1
    
    b = len(slist) - a
    c = len(tlist) - a
    
    print((a, b, c))
    

fun6()