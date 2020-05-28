# -*- coding: utf-8 -*-

import math
from functools import reduce
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

def solve():
    li = eval(input())    # [1, 234, 5, 6, 70, 890], [12,34,56,78,90]
    rli = []
    for elem in li:
        estr = str(elem)
        rli.append(int(estr[0]))
        rli.append(int(estr[-1]))
#    print(rli)
    
    rlen = len(rli)
    flag = [0] * rlen
    ans = []
    for i in range(rlen):
        ps = []              # 是prime
        notps = []           # 不是prime
        if flag[i] == 0 and is_prime(rli[i]):
            for j in range(i, rlen):
                if flag[j] == 0 and is_prime(rli[j]):
                    ps.append(rli[j])
                    flag[j] = 1
                else:
                    break
            if ps:
                ans.append(ps)
        elif flag[i] == 0:
            for j in range(i, rlen):
                if flag[j] == 0 and not is_prime(rli[j]):
                    notps.append(rli[j])
                    flag[j] = 1
                else:
                    break
            if notps:
                ans.append(notps)
    
    res = []
    for elem in ans:
        comb = reduce(lambda x,y:x*10+y, elem)
        res.append(comb)
    print(res)
    
solve()
