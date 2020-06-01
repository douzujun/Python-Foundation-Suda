# -*- coding: utf-8 -*-
"""
Created on Thu Mar 26 19:36:54 2020

@author: douzi
"""

    
def solve():
    n = int(input())
    count = 0
    res = []
#    datas = [('John', '2001/05/12'), ('Tom', '1814/09/06'), ('Ann', '2121/01/30'), ('James', '1814/09/05'), ('Steve', '1967/11/20')]
    for i in range(n):
        elem = input().split()
        if '1814/09/06' <= elem[1] <= '2014/09/06':
           res.append(elem) 
           count += 1
        
    res.sort(key=lambda x:x[1])

    if res:
        print(count, res[0][0], res[-1][0])
    else:
        print('0')
    
solve()