# -*- coding: utf-8 -*-

def statistics():
    n = int(input())
    
    res = []
    for i in range(n):
        data = input()
        name, stuId, score = data.split()
        res.append((name, stuId, int(score)))
        
    res.sort(key=lambda x:(x[2]))
    print(res[len(res) - 1][0], res[len(res) - 1][1])
    print(res[0][0], res[0][1])
    
statistics()