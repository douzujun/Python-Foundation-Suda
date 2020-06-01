# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 20:51:10 2020

@author: douzi
"""

def solve():
    N, M = input().split()
    N, M = int(N), int(M)
    
    nums = input().split()
    nums = list(map(int, nums))
    
    
    nums = nums[N-M:] + nums[:N-M]
    
    for i in range(0, N - 1):
        print(nums[i], end=' ')
        
    print(nums[N - 1])
    
solve()