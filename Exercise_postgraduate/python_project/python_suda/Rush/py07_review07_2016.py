#-*- coding: utf-8 -*-

import re
import math
import random

# 读出全部数据
def readDataFromFile(url):
    with open(url, 'r', encoding='utf8') as f:
        data = f.read()
        return data

# 素数判断
def is_prime(n):
    if n < 2:
        return False
    top = int(math.sqrt(n))    
    i = 2
    while i <= top:
        if n % i == 0:
            return False
        i = i + 1
    return True

# 3 或者 7
def judge(n):
    return '3' in str(n) or '7' in str(n)

# 输出素数
def printPrimes(primes):
    plen = len(primes)
    for i in range(plen):
        print('{0:>10}'.format(primes[i]), end='')
        if (i + 1) % 2 == 0:
            print('')
    print('')

# 组成坐标
def generatePoints(primes):
    plen = len(primes)
    points = [(primes[i], primes[i+1]) for i in range(0, plen - 1, 2)]
    return points

# 生成坐标A
def generateA():
    return [random.uniform(0, 100), random.uniform(0, 100)]

# 所有坐标到 A的距离
def distance(A, points):
    ans = []
    for p in points:
        ans.append( math.sqrt((A[0] - p[0])**2 + (A[1] - p[1])**2) )
    return ans

def ASCII(word):
    ans = 0 
    for w in word:
        ans += ord(w)
    return ans

def printWordsASCIIS(words):
    wlen = len(words)
    for i in range(wlen):
        print('{0:<8}'.format(ASCII(words[i])), end='')
        if (i + 1) % 10 == 0:
            print('')
    print('')

if __name__ == "__main__":
    data = readDataFromFile('./file/file_midterm_2016.txt') 

    nums = list(map(int, re.findall('[0-9]+', data)))
    primes = list(filter(lambda x: is_prime(x) and judge(x), nums))
    # 输出素数
    printPrimes(primes)

    points = generatePoints(primes)
    print(points)

    A = generateA()
    print('({0:>10.2f},{1:>10.2f})'.format(A[0], A[1]))

    distances = distance(A, points)
    print('欧式距离之和: {0:10.2f}'.format(sum(distances)))
    print('平均距离: {0:10.2f}'.format(sum(distances) / len(distances)))

    words = re.findall('[a-zA-Z]+', data)
    printWordsASCIIS(words)

