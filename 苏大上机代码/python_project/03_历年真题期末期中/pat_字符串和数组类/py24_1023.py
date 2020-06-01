# -*- coding: utf-8 -*-

from functools import reduce

def solve():
    line = input()
    lines = list(map(int, line.split()))
    
    res = []
    i = 0
    for e in lines:
        res.append(e*[i])
        i = i + 1
    
    data = []
    for i in range(0, 10):
        rlen = len(res[i])
        for j in range(0, rlen):
            data.append(res[i][j])
    
    if data[0] == 0:
        for i in range(0, len(data)):
            if data[i]:
                t = data[0]
                data[0] = data[i]
                data[i] = t
                break
    
    num = reduce(lambda x, y: x*10 + y, data)
    print(num)
    
solve()
    
    

