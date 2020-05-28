# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:49:09 2020

@author: douzi
"""

def int10(x):
    if x[0] == '0':
        return int(x, 8)
    return int(x)
    

def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        wds = f.read()
    return wds
    
def writeFile(url, trans):
    with open(url, 'w', encoding='utf8') as f:
        f.write(str(trans))

    
def main():
    wds = readFile('./file/file_2009.in')
    
    # 按照","分割字符串
    words = wds.split(',')
    # 去除空格
    words = [i.replace(' ', '') for i in words]
    
    trans = list(map(int10, words))
    trans.sort(reverse=True)    
    print(trans)
    
    writeFile('./file/file_2009.out', trans)
    
    
main()