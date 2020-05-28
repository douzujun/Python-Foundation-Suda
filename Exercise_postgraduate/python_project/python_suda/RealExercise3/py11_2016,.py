# -*- coding: utf-8 -*-

import re

def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
    return data

def train(words):
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
        
    return freq

def writeFile(sorted_freq):
    with open('./file/file_2016.out', 'w', encoding='utf8') as f:
        for elem in sorted_freq:
            if elem[1] > 5:
                f.write('{0}, {1}\n'.format(elem[0], elem[1]))

def main():
    data = readFile('./file/file_2016.in')
    words = re.findall('[a-zA-Z]+', data)
    print(words)
    
    freq = train(words)
    freq = sorted(freq.items(), key=lambda x:x[1], reverse=True)
    
    for elem in freq:
        if elem[1] > 5:
            print('{0}, {1}'.format(elem[0], elem[1]))
    
    writeFile(freq)
    
    
if __name__=='__main__':
    main()