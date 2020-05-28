# -*- coding: utf-8 -*-
"""
Created on Fri Mar  6 15:12:00 2020

@author: douzi
"""
import random
import re

def generateData(url):
    random.seed(1)
#    res = [i for i in range(1, 500)]   # 测试
    res = [random.randint(0, 2768) for i in range(0, 100)]
   
    with open(url, 'w', encoding='utf8') as f:
        for elem in res:
            f.write(str(elem) + " ")
            if (res.index(elem) + 1) % 10 == 0:
                f.write('\n')

# 读文件
def read_file(url):
    with open(url, 'r+', encoding='utf8') as f:
        data = f.read().split()
        data = list(map(int, data))
    return data
        

# 打印数组
def print_arr(alist, n):
    length = len(alist)
    for i in range(0, length):
        if i == 0:
            pass
        elif i % n == 0:
            print("")
        print("{0:6}".format(alist[i]), end='')
    
    print('\n')
    
    
# 统计数字0至9  在数组arr所有整数中的出现次数
def count(alist):
    res = [0 for i in range(0, 10)]
    length = len(alist)
    
    for i in range(0, length):
        num = list(str(alist[i]))    # 例: 123--> ['1', '2', '3']
        n_len = len(num)
        for j in range(0, n_len):
            res[int(num[j])] += num.count(num[j])
#    print(res)
    return res
    

# 因子和
def factor(n):
    res = 0
    for i in range(1, n+1):
        if n % i == 0:
            res += i
    return res

# 按照 因子和  从小到大排序，如果两个整数的因子和相等，则按照它们的自然大小排序
def sort_array(alist):
    alist.sort(key=lambda x:(factor(x), x))
    return alist

def filter_array(alist):
    arr = list(filter(lambda x:x%2==0, alist))
    arr.sort()
    arr.append(len(arr))
    return arr


def filter_fac(n):
    i = 2
    res = []
    while i <= n:
        if n % i == 0:
           res.append(i)
           n /= i
        else:
           i = i + 1
#    print(res)
    return res
            
    
def write_file(arr):
    with open('./file/file_2019_out.txt', 'w', encoding='utf8') as f:
        for elem in arr:
            fac = filter_fac(elem)
            fac = list(map(str, fac))
            print("{0}={1}".format(elem, "*".join(fac)))
            f.write("{0}={1}\n".format(elem, "*".join(fac)))


def main():
    url = './file/file_2019_in.txt'
    generateData(url)
    # 第一问
    data = read_file(url)
    print_arr(data, 10)
    
    # 第二问
    res = count(data)           # 统计数字0至9  在数组arr所有整数中的出现次数
    print_arr(res, 5)
    
    # 第(5)问
    data = sort_array(data)
    print(data)

    # 第(6)问
    arr = filter_array(data)
    print(arr)
    
    # 第(7)问
    write_file(arr)
    
    
main()



























