# -*- coding: utf-8 -*-

import random


# 找插入位置，使L仍保持升序
def find_insert_index(L, t):
    for i, x in enumerate(L):
        if x > t:
            return i
    
    return len(L)


A = [random.randint(0, 100) for i in range(10)]

print(A)

L = []

for x in A:
    i = find_insert_index(L, x)
    L.insert(i, x)

print(L)