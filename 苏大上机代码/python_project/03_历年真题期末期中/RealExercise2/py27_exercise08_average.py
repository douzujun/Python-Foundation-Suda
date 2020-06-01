# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 22:47:48 2020

@author: douzi
"""

import re

def sumAve(x):
    tmp = x
    cnt = 0
    res = 0 
      
    while tmp:
        res += tmp % 10
        tmp = tmp // 10
        cnt = cnt + 1
    return res / cnt

def func8():
    data = input()
    
    nums = map(int, re.findall('[0-9]+', data))
    nums = [elem for elem in nums if elem >= 100 and elem <= 99999]
    
    print(nums)
    
    nums.sort(key=lambda x:sumAve(x), reverse=True)
    print(nums)
    
    
func8()