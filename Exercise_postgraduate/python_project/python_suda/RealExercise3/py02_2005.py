# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 18:49:51 2020

@author: douzi
"""

import re

def word(text):
    return re.findall('[a-z]', text.lower())

def train(features):
    model = {}
    for f in features:
        model[f] = model.get(f, 0) + 1
        
    return model

def main():
    statistic = train(word(open('./file/file_2005_2.txt').read()))
    statistic = list(statistic.items())
    
    statistic.sort(key=lambda x:(x[1], x[0]), reverse=True)
    print(statistic)
    
    
if __name__=='__main__':
    main()