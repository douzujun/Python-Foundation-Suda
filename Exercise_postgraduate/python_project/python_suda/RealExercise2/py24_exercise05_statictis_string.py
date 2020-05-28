# -*- coding: utf-8 -*-
"""
Created on Fri Apr  3 20:16:07 2020

@author: douzi
"""

def train(features):
    model = {}
    for f in features:
        model[f] = model.get(f, 0) + 1
    
    return model
        

def fun5():
    text = input('输入字符串: ')
    print(text)
    freq = train(text.split())
    print(freq)
    
    freq = sorted(freq.items(), key=lambda x:(x[1], x[0]), reverse=True)
    
    freq = [elem[0] for elem in freq[:3]]
    print(freq)
    
    
fun5()