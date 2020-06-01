# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 23:20:30 2020

@author: douzi
"""

import math

def is_prime(num):
    if num < 2:
        return False
    top = math.sqrt(num)
    i = 2
    while i <= top:
        if num % i == 0:
            return False
        i = i + 1
    return True

def Reverse(num):
    return int(str(num)[::-1])

def print_res(res, length):
    for i in range(0, length):
        print('{0:>5}'.format(res[i]), end='')
        if (i + 1) % 8 == 0:
            print('')
    print('')
        
def main():
    cnt = 0
    cur = 2
    res = []
    while cnt < 30:
        if is_prime(cur) and is_prime(Reverse(cur)):
            res.append(cur)
            cnt = cnt + 1
        cur = cur + 1
    
    print_res(res, len(res))
    
    
if __name__=='__main__':
    main()