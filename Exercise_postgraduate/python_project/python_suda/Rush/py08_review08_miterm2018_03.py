# -*- coding: utf-8 -*-

import math
from functools import reduce

def is_prime(n):
    if n < 2:
        return False
    top = int(math.sqrt(n))
    i = 2
    while i <= top:
        if n % i == 0:
            return False
        i = i + 1
    return True

def splitByPrime(li):
    ans = []
    rlen = len(li)

    i = 0
    while i < rlen:
        no_pm = []
        flag = 0 
        j = i
        while j < rlen:
            if not is_prime(li[j]):
                no_pm.append(li[j])
            else:
                flag = 1
                break
            j = j + 1
        # 有非素数
        if no_pm:
            ans.append(reduce(lambda x, y: x*10+y, no_pm))
        if flag:
            while j < rlen:
                if is_prime(li[j]):
                    ans.append(li[j])
                else:
                    break
                j = j + 1
        i = j 
    return ans

def recombin(li):
    ans = []
    for e in li:
        es = str(e)
        ans.append(int(es[0]))
        ans.append(int(es[-1]))
    return ans 

def solve(li):
    comb = recombin(li) 
    print(comb)

    ans = splitByPrime(comb)
    print(ans)

if __name__ == "__main__":
    solve([1, 234, 5, 6, 7, 890])