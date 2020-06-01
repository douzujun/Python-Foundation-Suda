# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 19:45:38 2020

@author: douzi
"""

import math
import numpy as np

def fun4():
    li = eval(input("输入一个列表: "))
    
    print('list1: ', li)
    
    cnt = len(li)
    print("长度数目n*n: ", cnt)
    
    n = int(math.sqrt(cnt))     # m x n
    
    # 生成 nxn 的空矩阵
    res = [[] * n for i in range(n)]
    
    for i in range(n):
        for j in range(n):
            res[i].append(li[i * n + j])
        
    return res


res = fun4()
print(res)