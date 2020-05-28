# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:48:09 2020

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

def judge(num):
    a = list(str(num))
    return '9' not in a

def filterPrime(start, end):
    return [i for i in range(start, end + 1) if (is_prime(i) and judge(i))]

def save2file(url, text):
    with open(url, 'w+', encoding='utf8') as f:
        tlen = len(text)
        for i in range(tlen):
            f.write(str(text[i]) + ' ')
            if (i + 1) % 10 == 0:
                f.write('\n')
        
def main():
    res = []
    res = filterPrime(100, 1000)
    save2file('./file/file_2006.txt', res)
    
if __name__=='__main__':
    main()