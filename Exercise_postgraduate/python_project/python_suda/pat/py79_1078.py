# -*- coding: utf-8 -*-
"""
Created on Wed Mar 25 14:09:54 2020

@author: douzi
"""

import re

def solve():
    j = input()
    if j == 'C':      # 压缩
        data = input()
        data = [i+j for i,j in re.findall(r'([a-zA-Z\s])(\1*)', data)]
        res = ''
        for elem in data:
            res += str(len(elem))+elem[0] if len(elem) > 1 else elem[0]
        print(res)
    else:             # 解压
        data = input()
        data = re.findall('(\d*)([a-zA-Z\s])', data)
        res = ''
        for length, elem in data:
            if length == '':
                res += elem
            else:
                res += int(length)*elem
        print(res)
    
solve()