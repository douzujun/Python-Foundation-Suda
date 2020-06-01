# -*- coding: utf-8 -*-

import math

def judge_prime(num):
    if num < 2:
        return False
    
    top = int(math.sqrt(num))
    i = 2
    while i <= top:
        if num % i == 0:
            return False
        i = i + 1
        
    return True


def DFS(n, index=0, sum=0, primes=[], L=[], S=set()):
    if (sum > n):
        return
    
    # sum==n 找到了这样的一组数字
    if (index < len(primes)):
        if (sum == n):
            if (tuple(sorted(L)) not in S):
                print(L)
                S.add(tuple(sorted(L)))
                
        L.append(primes[index])
        
        # 可以重复选取
        DFS(n, index , sum + primes[index], primes, L, S)
        L.pop()
        DFS(n, index + 1, sum, primes, L, S)


def equal_prime(n):
    '''n拆分成素数之和'''
    plist = [i for i in range(n + 1) if judge_prime(i)]
    DFS(n, 0, 0, plist, S=set())
    
    

def main():
    while True:
        num = int(input())
        equal_prime(num)


main()















