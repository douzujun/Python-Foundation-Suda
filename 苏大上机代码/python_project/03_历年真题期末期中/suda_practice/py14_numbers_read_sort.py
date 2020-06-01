# -*- coding: utf-8 -*-

import numpy as np

def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
        data = data.split('\n')
    return data


def writeFile(url, data, mean, var):
    with open(url, 'w', encoding='utf8') as f:
        for e in data:
            f.write(str(e) + '\n')
            
        f.write(str(mean) + '\n')
        f.write(str(var) + '\n')
        

def main():
    data = readFile('./file/file13_numbers.txt')
       
    data = list(map(float, data))
    data.sort()
    
    mean = np.average(data)
    va = np.var(data)
    
    writeFile('./file/file13_numbers_out.txt', data, mean, va)
    
    
if __name__=='__main__':
    main()