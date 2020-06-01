# -*- coding: utf-8 -*-
"""
Created on Thu Mar 19 21:11:16 2020

@author: douzi
"""

def readFile(url):
    with open(url, 'r', encoding='utf8') as f:
        data = f.read()
    return data

def writeFile(url, data):
    with open(url, 'w', encoding='utf8') as f:
        for elem in data:
            f.write(elem + '\n')
            
def add_word(word, words):
    if word in words:
        return False
    wlen = len(words)    
    for i in range(0, wlen):
        if word > words[i]:
            words.insert(i+1, word)
            break
    writeFile('./file/file14_Names.txt', words)       
    
def main():
    data = readFile('./file/file14_Names.txt')
    print(data)
    
    words = data.split('\n')
    
    add_word('Abbott', words)
    
    
if __name__=='__main__':
    main()