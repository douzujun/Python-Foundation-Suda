# -*- coding: utf-8 -*-

def judge():
    n = int(input())
    
    A = {}
    B = {}
    res = [[0, 0, 0], [0, 0, 0]]
    for i in range(0, n):
        a, b = input().split()
        
        if (a == 'C' and b == 'J'):    # 甲胜
            res[0][0] += 1
            res[1][2] += 1
            A['C'] = A.get('C', 0) + 1
        elif (a == 'C' and b == 'C'):  # 甲平
            res[0][1] += 1
            res[1][1] += 1
        elif (a == 'C' and b == 'B'):  # 甲负
            res[0][2] += 1
            res[1][0] += 1
            B['B'] = B.get('B', 0) + 1
            
        elif (a == 'B' and b == 'C'):  # 甲胜
            res[0][0] += 1
            res[1][2] += 1
            A['B'] = A.get('B', 0) + 1
        elif (a == 'B' and b == 'B'):  # 甲平
            res[0][1] += 1
            res[1][1] += 1
        elif (a == 'B' and b == 'J'):  # 甲负
            res[0][2] += 1
            res[1][0] += 1
            B['J'] = B.get('J', 0) + 1
     
        elif (a == 'J' and b == 'B'):  # 甲胜
            res[0][0] += 1
            res[1][2] += 1
            A['J'] = A.get('J', 0) + 1
        elif (a == 'J' and b == 'J'):  # 甲平
            res[0][1] += 1
            res[1][1] += 1
        elif (a == 'J' and b == 'C'):  # 甲负
            res[0][2] += 1
            res[1][0] += 1
            B['C'] = B.get('C', 0) + 1   
            
    A = sorted(A.items(), key=lambda x:(-x[1], x[0]))
    B = sorted(B.items(), key=lambda x:(-x[1], x[0]))
    
    alen = len(res[0])
    blen = len(res[1])
    for i in range(0, alen - 1):
        print(res[0][i], end=' ')
    print(res[0][i])
    
    for i in range(0, blen - 1):
        print(res[1][i], end=' ')
    print(res[1][i])
    
    print(A[0][0], B[0][0])


judge()
    
    