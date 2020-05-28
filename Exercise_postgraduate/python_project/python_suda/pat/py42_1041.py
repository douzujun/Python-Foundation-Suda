# -*- coding: utf-8 -*-

def solve():
    N = int(input())
    
    res = []
    for i in range(N):
        line = input()
        res.append(tuple(line.split()))
    
    rlen = len(res)
    
    M = int(input())
    line = input().split()
 
    ans = ''       
    for i in range(M - 1):
        for j in range(rlen):
            if line[i] == res[j][1]:
                ans += res[j][0] + ' ' + res[j][2] + '\n'
                break
            
    for j in range(rlen):
        if line[M - 1] == res[j][1]:
            ans += res[j][0] + ' ' + res[j][2]
            break
        
    print(ans)
    
solve()