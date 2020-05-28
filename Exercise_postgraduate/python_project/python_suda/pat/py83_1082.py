# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 22:54:06 2020

@author: douzi
"""

def distance(a, target):
    return (abs(a[0] - target[0])**2 + abs(a[1] - target[1])**2)

def solve():
    n = int(input())
    
    stu = []
    for i in range(n):
        data = input().split()
        stu.append((data[0], (int(data[1]), int(data[2])) ))
    
    stu.sort(key=lambda x:(distance(x[1], (0, 0))))
    print(stu[0][0], stu[-1][0])
    
    
solve()