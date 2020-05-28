# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:48:37 2020

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

# 123--->321
def reverseNum(num):
    res = int(str(num)[::-1])
    return res

# 筛选素数
def filter_prime(start, end):
    return [i for i in range(start, end + 1) if is_prime(i) and is_prime(reverseNum(i))]


def saveFile(url, text):
    with open(url, 'r+', encoding='utf8') as f:
        tlen = len(text)
        for i in range(tlen):
            f.write(str(text[i]) + ' ')
            if (i + 1) % 10 == 0:
                f.write('\n')

def main():
    res = filter_prime(10, 1000)
    print(res)
    saveFile('./file/file_2007.txt', res)
    
if __name__=='__main__':
    main()