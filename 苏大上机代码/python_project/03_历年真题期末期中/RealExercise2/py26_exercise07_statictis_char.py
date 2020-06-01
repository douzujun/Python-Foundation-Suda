# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 21:35:58 2020

@author: douzi
"""

import re

def func7():
    s = input().upper()
    words = re.findall('[a-zA-Z]', s)
    
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    
    freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
    print(freq[0])
    
        
func7()