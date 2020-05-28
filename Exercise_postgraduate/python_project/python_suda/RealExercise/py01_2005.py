# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 21:40:42 2020

@author: douzi
"""

import math

def is_prime(num):
    if num < 2:
        return False
    
    top = int(math.sqrt(num))
    i = 2
    while i <= top:
        if num % i == 0:
            return False
        i = i + 1
        
    return True
    

res = []
# 从大到小 继续筛选
def split_prime(num):
    if num < 2:
        return
    
    if is_prime(num):
#        print(num)
        res.append(num)
        return
        
    for i in range(num, 1, -1):
        if (is_prime(i) and num - i > 1):
            res.append(i)
            split_prime(num - i)
            return 
    

def faction_prime():
    while True:
        num = int(input())
        split_prime(num)
        print(res)
        res.clear()
        
    
def main():
    faction_prime()
    
        
if __name__=='__main__':
    main()
    
    
    
    
    
    