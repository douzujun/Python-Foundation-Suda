# -*- coding: utf-8 -*-

def solve():
    x, y = eval(input())

    if (x == 1 and -1 < y < 1) or (x == -1 and -1 < y < 1) \
        or (y == -1 and -1 < x < 1) or (y == 1 and -1 < x < 1):
            return 0
    elif (x > 1) or (x < -1) or (y > 1) or (y < -1):
        return -1
    else:
        return 1

print(solve())
