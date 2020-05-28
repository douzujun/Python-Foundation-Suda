# -*- coding: utf-8 -*-
"""
Created on Fri Apr 10 18:27:21 2020

@author: douzi
"""

import random

def generateData(url):
    random.seed(100)
    # 测试
#    res = [random.randint(0, 10) for i in range(10)]
    res = [random.randint(0, 2768) for i in range(100)]
    
    with open(url, 'w', encoding='utf8') as f:
        rlen = len(res)
        for i in range(rlen):
            f.write(str(res[i]) + ' ')
            if (i + 1) % 10 == 0:
                f.write('\n')
    
def readFile(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read().split()
        data = list(map(int, data))
    return data
    
# 打印数组
def print_arr(alist, n):
    length = len(alist)
    for i in range(0, length):
        print('{0:6}'.format(alist[i]), end='')
        if (i + 1) % n == 0: 
            print('')
    print('')


# 编写函数count： 统计数字0至9 在数组arr所有整数中的出现次数，
# 将结果放入数组res中（即res[0]存储数字0的出现次数，res[1]存储数字1的出现次数，其余以此类推）
def count(alist):
    res = [0 for i in range(0, 10)]
    length = len(alist)
    
    for i in range(0, length):
        num = list(str(alist[i]))
        nlen = len(num)              # 123-->['1', '2', '3']
        for j in range(0, nlen):
            res[int(num[j])] += 1    
    return res

def factor(num):
    res = 0
    i = 1
    while i <= num:
        if num % i == 0:
            res += i
        i = i + 1
    return res

def sort_array(alist):
    alist.sort(key=lambda x:(factor(x), x))      
    return alist

def filter_array(alist):
    alist = list(filter(lambda x:x%2 == 0, alist))
    alist.sort()
    alist.append(len(alist))
    return alist

def filter_fac(elem):
    i = 2
    res = []
    while elem != 1:
        if elem % i == 0:
            res.append(i)
            elem = elem // i
        else:
            i = i + 1
    return res

def writeFile(alist):
    with open('./file/file_2019.out', 'w', encoding='utf8') as f:
        for elem in alist:
            fac = filter_fac(elem)
            ans = '*'.join(list(map(str, fac)))
            print('{0}={1}'.format(elem, ans))
            f.write('{0}={1}\n'.format(elem, ans))

def main():
    generateData('./file/file_2019.txt')
    data = readFile('./file/file_2019.txt')
    print_arr(data, 10)

    res = count(data)
    print_arr(res, 5)
    
    fac_sorted = sort_array(data)
    print_arr(fac_sorted, 10)
    
    even_array = filter_array(data)
    print_arr(even_array, 10)
    
    writeFile(even_array[:-1])
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    