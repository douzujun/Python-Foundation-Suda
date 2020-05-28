# -*- coding: utf-8 -*-
"""
Created on Sat Apr  4 19:49:26 2020

@author: douzi
"""

import math
import random
import struct

def generateData():
#    random.seed(100)
    res = [random.randrange(0, 9999, 1) for i in range(0, 16)]
    rlen = len(res)    
    
    with open('./file/file_2010.txt', 'rb+') as f:
        for i in range(rlen):
            s = struct.pack('i', res[i])
            f.write(s)
    
    nums = []
    with open('./file/file_2010.txt', 'rb+') as f:
        for i in range(rlen):
            data = f.read(4)
            elem = struct.unpack('i', data)[0]
            nums.append(elem)
    return nums

def is_prime(num):
    if num < 2:
        return False
    top = int(math.sqrt(num))
    i = 2
    while i <= top:
        if num % i == 0:
            return False
        i = i + 1
    return True

def main():
    data = generateData()
    print(data)
    
    data.sort(reverse=True)
    print(data[0], data[-1])
    
    for i in data:
        if is_prime(i):
            print("最大素数: ", i)
            break
    
    dlen = len(data)
    mid = data[dlen//3 : dlen//3*2]
    print(mid[0], mid[-1])


if __name__=='__main__':
    main()