# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 18:23:03 2020

@author: douzi
"""

def matrixMul(A, B):
    if len(A[0]) == len(B):                               # A列数 == B行数
        res = [[0] * len(B[0]) for i in range(len(A))]    # A行 x B列
        for i in range(len(A)):
            for j in range(len(B[0])):
                for k in range(len(B)):         # (A列)B行
                    res[i][j] += A[i][k] * B[k][j]
        return res
    return ("输入矩阵有误!")
    
def fun3():
    mat1 = eval(input("mat1: "))
    mat2 = eval(input("mat2: "))
    
    result = matrixMul(mat1, mat2)
    
    # 矩阵乘法
    print(result)
    
fun3()