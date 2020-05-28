# -*- coding: utf-8 -*-

import re

def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
        return data


def lessSpace(s):
    words = re.findall('[a-zA-Z]+|[.?!]', s)
    print(words)
    res = ''
    for word in words:
        if word.isalpha():
            res += word + ' '
        else:
            res = res[:-1]
            res += word + ' '
            
    if not res[-2].isalpha():
        return res[:-1]
    else:
        return res

def main():
    data = readFile('./file/file10_space.txt')
    words = lessSpace(data)    
    print(words)
    
if __name__=='__main__':
    main()