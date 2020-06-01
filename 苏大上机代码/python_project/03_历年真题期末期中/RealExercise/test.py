# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 20:22:14 2020

@author: douzi
"""

#import struct
#
#def readFile(url):
#    ls=[]
#    with open(url, 'rb+') as f:
#        for i in range(32):
#            data = f.read(4)
#            elem = struct.unpack('i', data)[0]
#            ls.append(elem)
#    return ls
#
#if __name__=='__main__':
#    data = readFile("./file/test.bat")     #读的是文本文件
#    print(data)

import math
import string

def judgePrime(x):
    '''
    function: 判断一个整数是否为素数
    input: 一个正整数 x
    output：如果x是素数，则返回ture， 否则返回false
    '''
    n = int(math.sqrt(x) + 1)
    for i in range(2, n + 1):
        if x % i == 0:
            return False
    return True

def main():
    #打开二进制文件读取数据
    dataL = list()
    with open('./file/2010.txt', 'rb') as fp:
        #假设数据存在多行
        temp1 = fp.readlines()
        temp2 = "".join(temp1)
        f = lambda x : int(x)
        dataL = list(map(f, temp2))
    
    #删除数据当中为0的数
    while dataL[-1] == 0:
        dataL.pop()
        
    n = len(dataL)
    minNum = min(dataL)
    maxNum = max(dataL)
    
    #得到数据当中的最大素数
    maxPrime = 0
    for item in dataL:
        if judgePrime(item):
            maxPrime = max(maxPrime, item)
    
    
    dataL.sort(reverse = True)
    
    #将数据的个数变成3的倍数
    temp = n % 3
    while temp > 0:
        dataL.pop()
    
    Len = len(dataL)
    m = Len // 3
    index = 2*m
    mid_dataL = dataL[m:index]
    
    mid_maxNum = max(mid_dataL)
    mid_minNum = min(mid_dataL)
    
    
    print('n = {0}'.format(n))
    print('max = {0}'.format(maxNum))
    print('min = {0}'.format(minNum))
    print('max_prime = {0}'.format(maxPrime))
    print('min in mid_seg = {0}'.format(mid_minNum))
    print('max in mid_seg = {0}'.format(mid_maxNum))
    
    
if __name__ == '__main__':
    main()