# -*- coding: utf-8 -*-
 

def matrixMul(A, B):
    if len(A[0]) == len(B):  # A列数=B行数
        res = [[0] * len(B[0]) for i in range(len(A))]  # 生成 A行 x B列 的 0矩阵
        for i in range(len(A)):
            for j in range(len(B[0])):                  
                for k in range(len(B)):                  # (A列)B行
                    res[i][j] += A[i][k] * B[k][j]       # 矩阵乘法
        return res
    return ("输入矩阵有误!")

def fun3():
    mat1 = eval(input("输入矩阵mat1:"))
    mat2 = eval(input("输入矩阵mat2:"))
    result = matrixMul(mat1, mat2)
    # 矩阵乘法 结果
    print(result)
    

if __name__ == '__main__':
    fun3()
    
    
    