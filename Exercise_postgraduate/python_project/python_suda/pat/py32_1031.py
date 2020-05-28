# -*- coding: utf-8 -*-
"""
Created on Tue Mar 24 21:42:51 2020

@author: douzi
"""

import re

M = ['1', '0', 'X', '9', '8', '7', '6', '5', '4', '3', '2']
def weight(num):
    w = [7,9,10,5,8,4,2,1,6,3,7,9,10,5,8,4,2]
    wei = 0
    wlen = len(w)
    for i in range(0, wlen):
        wei += w[i] * num[i]
        
    return wei % 11

def main():
    
    n = int(input())
    i = 0
    flag = 0
    res = []
    while i < n:
        num = input()
        
        # 匹配前17个
        if re.match('[0-9]{17}.', num):
            idNum = list(map(int,list(num[:17])))
            wei = weight(idNum)    # 求权重
            if num[-1] != M[wei]:  # 对照M 匹配
                res.append(num)
                flag += 1
        else:
            res.append(num)
            flag += 1
        i = i + 1
        
    if not flag:
        print("All passed")
    else:                        # 全部匹配 
        for e in res:
            print(e)
        
main()
    
    