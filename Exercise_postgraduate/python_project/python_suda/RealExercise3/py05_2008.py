# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:48:55 2020

@author: douzi
"""

import re

def train():
    with open('./file/file_2008.txt', encoding='utf8') as f:
        wds = f.read()
        
    wds = re.findall('[a-zA-Z]+', wds)
    print(wds)
    
    wds = [i.capitalize() for i in wds if i.lower() != 'the']
    print('\n', wds)
    
    with open('./file/file_2008.txt', 'w+', encoding='utf8') as f:
        for word in wds:
            f.write(word + '\n')
    
    
train()