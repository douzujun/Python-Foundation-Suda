# -*- coding: utf-8 -*-

def func1():
    m = eval(input("输入m:\n"))
    n = eval(input("输入n:\n"))
    
    if (m <= 1 or n <= 1):
        return None
    
    if m < n:
        m, n = n, m
        
    return m % n

print(bool(func1()))
