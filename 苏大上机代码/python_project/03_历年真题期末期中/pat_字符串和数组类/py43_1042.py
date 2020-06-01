# -*- coding: utf-8 -*-

import re

def solve():
    s = input().lower()
    words = re.findall('[a-zA-Z]', s)
    
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        
    freq = sorted(freq.items(), key=lambda x:(-x[1], x[0]))
    print(freq[0][0], freq[0][1])
    
solve()