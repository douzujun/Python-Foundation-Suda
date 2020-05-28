# -*- coding: utf-8 -*-

import re

def solve():
    n = int(input())
    dic = {'A':'1', 'B':'2', 'C':'3', 'D':'4'}    
    res = ''
    for i in range(n):
        line = input()
        T = re.findall('(.)-T', line)[0]
        res += dic[T]
    
    print(res)
    
solve()
                

