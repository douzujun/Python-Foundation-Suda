# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:49:59 2020

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

def judge(num):
    unit = num % 10    # 个位
    decade = (num // 10) % 10  # 十位
    hund = (num // 100) % 10
    return [unit, decade, hund]


def comb(a, b):
    return a * 10 + b


def filter_prime(start, end):
    res = [i for i in range(start, end + 1) if is_prime(i) and 
           is_prime(comb(judge(i)[1], judge(i)[0])) and
           is_prime(comb(judge(i)[2], judge(i)[0])) and
           is_prime(comb(judge(i)[0], judge(i)[1])) and
           is_prime(comb(judge(i)[0], judge(i)[1])) and
           is_prime(comb(judge(i)[0], judge(i)[2]))]
    return res
    
def main():
    res = filter_prime(1000, 9999)
    print(res)
    
if __name__=='__main__':
    main()