# -*- coding: utf-8 -*-


def solve():
    n = input()
    
    words = n.split()
    
    print(' '.join(words[::-1]))


solve()
