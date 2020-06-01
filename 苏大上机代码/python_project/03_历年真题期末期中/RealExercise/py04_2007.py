# -*- coding: utf-8 -*-

import math

def is_prime(num):
    top = math.sqrt(num)
    i = 2
    
    while i <= top:
        if num % i == 0:
            return False
        i = i + 1
    
    return True

def reverseNum(num):
    res = int("".join(list( list(reversed(str(num))) ) ))
    return res


def filter_prime(start, end):
    return [i for i in range(start, end+1) if is_prime(i) and is_prime(reverseNum(i))]


def saveFile(text):
    with open("./file/2007.txt", 'w', encoding='utf8') as f:
        f.write(str(text))


def main():
    res = filter_prime(10, 1000)
    print(res)
    saveFile(res)
    
    
if __name__=='__main__':
    main()
