# -*- coding: utf-8 -*-

def fun1():
    for i in range(100, 1001):
        sum = 0
        for j in range(1, i):
            if (i % j == 0):
                sum += j
        if sum == i:
            print(i)
            
fun1()