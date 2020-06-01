# -*- coding: utf-8 -*-

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

def judge():
    data = input().split()
    M, N = int(data[0]), int(data[1])
    
    primes = [i for i in range(2, 1000125) if is_prime(i)]
    
    primes = [str(primes[i]) for i in range(M-1, N)]
    
    plen = len(primes)
    
    row = (plen+10) // 10
    s = 0
    for i in range(0, row):
        line = ' '.join(primes[s:s+10])
        print(line)
        s += 10
    
judge()