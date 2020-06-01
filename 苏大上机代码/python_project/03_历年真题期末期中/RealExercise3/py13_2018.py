# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 16:36:06 2020

@author: douzi
"""

import random
import struct

def GenerateData(url):
    random.seed(100)
    #    res = (random.randint(2,20000) for i in range(0, 20000))
#    res = [11, 3, 5, 7, 9, 12, 33, 31, 4, 11]
    res = [2,3,5,7,13,17,23,29,31,37,41,43, 9]
    with open(url, 'wb+') as f:
        for elem in res:
            s = struct.pack('i', elem)
            f.write(s)
            
def readFile(url):
    with open(url, 'rb+') as f:
        res = []
        while True:
            data = f.read(4)
            if not data:
                break
            elem = struct.unpack('i', data)[0]
            res.append(elem)
        return res
    
def gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    
    while num1 % num2:
        temp = num1 % num2
        num1 = num2
        num2 = temp
    return num2


def filter_list(data, length):
    res = []
    print(data)
    
    flag = [1 for i in range(0, length)]
    for i in range(length):
        for j in range(i+1, length):
            if gcd(data[i], data[j]) != 1:
                flag[j] = flag[i] = 0
                break
        if flag[i] and (j == length - 1) and (gcd(data[i], data[j - 1]) == 1):
            res.append(data[i])
            print('res:', res)
            
    res = list(set(res))
    print(res, len(res))

    return res


def writeFile(res, length):
    with open('./file/file_2018.out', 'w', encoding='utf8') as f:
        for i in range(length):
            f.write(str(res[i]) + ' ')
            if (i + 5) % length == 0:
                f.write('\n')
        

def main():
    url = './file/file_2018.in'
    
    GenerateData(url)
    data = readFile(url)
    
    length = len(data)
    res = filter_list(data, length)
    
    writeFile(res, len(res))
    
if __name__=='__main__':
    main()
    




























