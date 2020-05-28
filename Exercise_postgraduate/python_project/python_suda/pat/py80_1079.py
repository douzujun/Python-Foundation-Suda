# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 23:40:56 2020

@author: douzi
"""

def reverseNum(num):
    nums = str(num)[::-1]
    return nums

def isPlalind(num):
    nlen = len(num)
    for i in range(nlen):
        if num[i] != num[nlen - i - 1]:
            return False
    return True
        

def solve():
    n = input()
    
    i = 0
    while i < 10:
        rev = reverseNum(n)
        adds = int(n) + int(rev)
        if isPlalind(str(adds)):
            print("{0} + {1} = {2}".format(n, rev, adds))
            print("{0} is a palindromic number.".format(adds))
            break
        else:
            print("{0} + {1} = {2}".format(n, rev, adds))
        n = str(adds)
        i = i + 1
        
    if i == 10:
        print("Not found in 10 iterations.")
    
    
solve()