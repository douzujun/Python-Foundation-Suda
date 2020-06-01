# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 21:43:39 2020

@author: douzi
"""

import math

def solve():
    M = int(input())    
    
    data = list(map(int, input().split()))

    for K in data:
        for N in range(1, 10):
            t = N * K**2
            if t % 1000 == K or t % 100 == K or t % 10 == K:
                print(N, N * K**2)
                break
        else:
            print('No')

solve()