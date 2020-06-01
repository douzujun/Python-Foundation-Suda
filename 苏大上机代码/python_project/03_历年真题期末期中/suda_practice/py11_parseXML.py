# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 17:37:05 2020

@author: douzi
"""


import re

def readFile(url):
    with open(url, 'r', encoding='utf8') as f:
        data = f.read()
    return data

def parseXML(s):
    res = re.findall('<(.*)>(.*)</.*>', s)
    for word in res:
        print("{0}: {1}".format(word[0], word[1]))

def main():
    data = readFile('./file/file11_parse.txt')
    print(data)
    
    parseXML(data)
    
    
if __name__=='__main__':
    main()