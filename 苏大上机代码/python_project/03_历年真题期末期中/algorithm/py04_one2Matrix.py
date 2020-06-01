# -*- coding: utf-8 -*-

import math
import numpy as np


def fun4():
    # 输入数据, 例如: [2,1,4,5]
    li = eval(input("输入一个列表:"))
    print("list1:", li)
    
    cnt = len(li)
    print("长度数目n*n: ", cnt)
    
    n = int(math.sqrt(cnt))    # n x n
    
    # 生成 nxn 的 空矩阵
    res = [[] * n for i in range(0, n)]
    
    for i in range(0, n):
        for j in range(0, n):
            # 添加第i行,j列元素
            res[i].append(li[i * n + j])
    
    return res


res = fun4()
print(res)




