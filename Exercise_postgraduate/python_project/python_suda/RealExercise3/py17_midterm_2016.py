# -*- coding: utf-8 -*-
"""
Created on Sat Apr 11 20:38:58 2020

@author: douzi
"""

import math
import re
import random

def is_prime(n):
    if n < 2:
        return False
    top = math.sqrt(n)
    i = 2
    while i <= top:
        if n % i == 0:
            return False
        i = i + 1
    return True

def judge(n):
    li = list(n)
    return '3' in li or '7' in li

def readFile(url):
    with open(url, 'r', encoding='utf8') as f:
        data = f.read()
    return data
    
def generateA():
    random.seed(100)
    a = random.uniform(0, 101)
    b = random.uniform(0, 101)
    return (a, b)

def distance(a, target):
    return math.sqrt((a[0]-target[0])**2 + (a[1]-target[1])**2)   
    
def ASCII(word):
    ids = 0
    for w in word:
        ids += ord(w)
    return ids

def main():
    data = readFile('./file/file_midterm_2016.txt')
    print(data)
    
    # 提取所有整数
    num = re.findall('[0-9]+', data)
    # 判断素数 and 判断素数包含数字3或7
    primes = [int(elem) for elem in num if is_prime(int(elem)) and judge(elem)]
    for elem in primes:
        # 每个值占10列、右对齐、每行显示2个数
        print("{0:>10}".format(elem), end=' ')
        if (primes.index(elem)) % 2:
            print('')
    
    print('')
    # 排序坐标
    primes.sort()
#    print(primes)
    
    plen = len(primes)
    plen = plen if (plen % 2 == 0) else plen - 1
    
    # 所有坐标
    points = [(primes[i], primes[i+1]) for i in range(0, plen-1, 2)]
#    print(points)    
    # 随机数构成的坐标点输出格式
    A = generateA()
    print("({0:>10.2f}, {1:10.2f})".format(A[0], A[1]))
    
    # 计算所有坐标点到A之间的欧式距离之和
    dis = []
    for i in range(0, plen//2):
        d = distance(points[i], A)
        dis.append(d)
    print("距离之和: {0:.2f}".format(sum(dis)))
    print("平均距离为:{0:10.2f}, 素数构成坐标点数为:{1:10.2f}".format(sum(dis) / len(dis), plen//2))
    
    # 提取所有单词
    words = re.findall('[a-zA-Z]+', data)
    print(words)
    
    print("单词转化成整数:")
    wlen = len(words)
    ascii_words = [ASCII(elem) for elem in words]
    for i in range(0, wlen):
        print('{0:8}'.format(ascii_words[i]), end='')
        if (i+1) % 10 == 0:
            print('')
  
main()
