# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:14:09 2020

@author: douzi
"""

def fun2():
    li = eval(input("list: "))
    Len = len(li)
    
    cnt = 0
    
    for i in range(0, Len):
        for j in range(i, Len):
            if (li[i] > li[j]):
                cnt += 1
    
    
    print(cnt)
    
fun2()
    