# -*- coding: utf-8 -*-

def solve():
    s = input()
    for e in s:
        if e.isupper():
            s = s[0].upper() + s[1:].lower()
            return s
    if s.islower():
        return s[0].upper() + s[1:-1].lower() + s[-1].upper()
    
print(solve())