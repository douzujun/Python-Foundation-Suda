# -*- coding: utf-8 -*-


def allsum(n):
    nl = list(str(n))
    res = 0
    for e in nl:
        res += int(e)
    return res

def allMul(n):
    nl = list(str(n))
    res = 1
    for e in nl:
        res *= int(e)
    return res

def fun1(num):
    nsum = allsum(num)
    nmul = allMul(num)
    
    print(nmul - nsum)
    
fun1(234)
    
    