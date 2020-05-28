# -*- coding: utf-8 -*-

import collections
import itertools

def func4(mat):
    m=len(mat)
    mm=[[0 for i in range(m)] for j in range(2*m-1)]    

    for i in range(m):
        for j in range(m):
            if i+j<m:
                mm[i+j][j]=mat[i][j]
            else:
                mm[i+j][m-i-1]=mat[i][j]
    return mm

def solve():
    A = eval(input()) # [[1,2,3], [4,5,6], [7,8,9]]
    m = len(A)
    B = [[0]*m for i in range(2*m-1)]
    row = 2*m - 1
    
    dic = collections.defaultdict(list)
    for i,j in itertools.product(range(m), range(m)):
        dic[i - j].append(A[m-i-1][j])

    dic = sorted(dic.items(), key=lambda x:x[0], reverse=True)
    print(dic)
    
    for i in range(row):
        rlen = len(dic[i][1])
        for j in range(rlen):
            B[i][j] = dic[i][1][j]
            
    print(B)
    
solve()

#print(func4([[1,2,3], [4,5,6], [7,8,9]]))
