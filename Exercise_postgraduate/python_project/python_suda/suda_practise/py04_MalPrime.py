# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 15:02:13 2020

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

def is_MalPrime(num):
    return is_prime(num) and is_prime(2**num-1)
    

def filter_prime():
    cur = 2
    res = []
    # 注意是 2^cur <= 1000
    while math.pow(2,cur) <= 1000:
        if is_MalPrime(cur):
            res.append(cur)
        cur = cur + 1
    
    return res

def print_res(res, length):
    for i in range(0, length):
        print("{0:>3} {1:>4}".format(res[i], 2**res[i]-1))

def main():
    res = filter_prime()
    print_res(res, len(res))
    
if __name__=='__main__':
    main()