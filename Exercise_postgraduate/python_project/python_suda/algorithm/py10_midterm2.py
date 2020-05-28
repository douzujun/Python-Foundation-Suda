# -*- coding: utf-8 -*-
"""
Created on Sat Mar 14 14:51:13 2020

@author: douzi
"""

def func2(lst : list):
    flag = {}
    for e in lst:
        flag[e] = flag.get(e, 0) + 1
        
    res = []
    for e in flag.values():
       res.append(e)
       
    rlen = len(res)
    for i in range(0, rlen):
        for j in range(i+1, rlen):
            if res[i] == res[j]:
                return False
    return True

def main():
    print(func2([1,2,2,1,1,3]))
    print(func2([1,2,2,1,1,3,3]))
    print(func2([1,2,2,1,1,3, 4,4,4]))
    print(func2([1,2,2,1,1,3, 4,4,4,4,4]))
    
main()