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


# 不含9
def judge(num):
    a = list(str(num))
    return '9' not in a


def filterPrime(start, end):
    return [i for i in range(start, end + 1) if (is_prime(i) and judge(i))]


def save2file(text):
    print(text)
    
    with open('./file/2006.txt', 'w+', encoding='utf8') as f:
        f.write(text)


def main():
    res = []
    res = filterPrime(100, 1000)
    save2file(str(res))
    
    
if __name__=='__main__':
    main()
    
    
    
    