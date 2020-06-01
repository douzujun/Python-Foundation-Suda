# -*- coding: utf-8 -*-
"""
Created on Sun Mar 22 19:57:26 2020

@author: douzi
"""

# 2016 python期中考试编程题

import math
import re
import random

def is_prime(num):
    if num < 2:
        return False
    top = math.sqrt(num)
    i = 2
    
    while i <= top:
        if num % i == 0:
            return False
        i = i + 1
    return True

# 读数字
def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read()
    return data

# 包含数字3 或 数字7
def judge(num):
    li = list(num)
    return '3' in li or '7' in li

# 随机数构成的坐标点输出格式
def generateA():
    random.seed(100)
    a = random.uniform(0, 101)
    b = random.uniform(0, 101)
    return (a, b)

# 计算欧式距离
def distance(a, b):
    return math.sqrt(math.pow(abs(a[0]-b[0]), 2) + math.pow(abs(a[1]-b[1]), 2))

# ASCII之和
def ASCII(word):
    res = 0
    li = list(word)
    for w in li:
        res += ord(w)
    return res

def main():
    data = readFile('./file/file_midterm2016.txt')
    
    # 1. 提取所有数
    nums = re.findall('\d+', data)
    print(nums)
    
    # 提取第一步中string中包含数字3 或 数字7的所有素数 
    primes = [int(elem) for elem in nums if is_prime(int(elem)) and judge(elem)]
    print(primes)
    
    # 并将满足条件的素数 显示在屏幕上，要求每个值 占10列，右对齐，每行显示2个数
    for elem in primes:
        print("{0:>10}".format(elem), end=' ')
        if (primes.index(elem) + 1) % 2 == 0:
            print('')
    print('')
    
    # 排序坐标
    primes.sort()
    
    plen = len(primes)
    plen = plen if (plen % 2 == 0) else plen - 1
    
    points = [(primes[i], primes[i+1]) for i in range(0, plen-1, 2)]
    print(points)
    
    # 随机数构成的坐标点输出格式
    A = generateA()
    
    # 计算所有坐标点到A之间的欧式距离之和
    dis = []
    for i in range(0, plen // 2):
        d = distance(points[i], A)
        dis.append(d)
    print("距离之和: {0:.2f}".format(sum(dis)))
    print("平均距离为:{0:10.2f}, 素数构成坐标点数为:{1:10.2f}".format(sum(dis) / len(dis), plen//2))
    
    # 提取string中的所有单词，其中连续的字符串成为一个单词
    # 将所有字母的 ASCII之和 显示在屏幕上，要求每行显示10个整数，每个整数占8列，左对齐
    words = re.findall('[a-zA-Z]+', data)
    print(words)
    
    print("单词转化成整数:")
    wlen = len(words)
    # Regular: R,e,g,g,l,a,r的ASCII之和
    ascii_word = [ASCII(elem) for elem in words]
    for i in range(0, wlen):
        print("{0:8}".format(ascii_word[i]), end='')
        if (i+1) % 10 == 0:
            print('')
         
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
        