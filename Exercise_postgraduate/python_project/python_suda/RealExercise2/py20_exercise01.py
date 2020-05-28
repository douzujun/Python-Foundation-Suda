# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 17:58:08 2020

@author: douzi
"""

def fun1():
    m = eval(input("m:"))
    n = eval(input("n:"))
    
    if (m <= 1 or n <= 1):
        return None
    
    if m < n:
        m, n = n, m
    
    return m % n

print(bool(fun1()))