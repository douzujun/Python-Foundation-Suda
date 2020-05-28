# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 21:47:27 2020

@author: douzi
"""
import re

def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read().lower()
    return data

def train(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return freq

def main():
    data = readFile('./file/file07_statistic.txt')
    words = re.findall('[a-zA-Z]', data)
    print(words)    
    
    freq = train(words)
    print(freq)
    
    
if __name__=='__main__':
    main()