# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 19:33:35 2020

@author: douzi
"""
# 2019真题 python版本
#已知：数据文件data.txt是一个文本文件，其中存放了 100个 不超过32768 的 非负整数。
#请编写程序完成如下功能：
#(1) 编写函数 read_file 从文件中 读取数据，将 所有的整数 按照 其 在文件中出现的顺序 依次存储到数组arr中；
#(2) 编写函数print：将数组arr显示在屏幕上， 每行显示n个数， 每个整数占6列；
#(3) 编写函数count： 统计数字0至9 在数组arr所有整数中的出现次数，
# 将结果放入数组res中（即res[0]存储数字0的出现次数，res[1]存储数字1的出现次数，其余以此类推）； 
#(4) 编写函数print_res：将数组res显示在屏幕上，每行显示5个数，可以复用步骤(2)中print函数；
#(5) 编写函数sort_array ：将数组arr中的整数 按照 因子和 从小到大排序，如果两个整数的因子和相等，
# 则按照它们的自然大小排序（注意：计算一个整数的因子和时 包括1和其本身）；
#(6) 编写函数filter_array： 对数组arr中的整数 进行 筛选，结果继续保存在arr中，筛选规则如下：
# 保留所有的偶数，同时保证这些偶数按照从小到大排序。
# 说明：完成筛选之后，数组arr中的元素可以分成两部分：
#  - 前半部分是有效内容，即所有的偶数
#  - 后半部分则是无效内容，参数size记录了数组arr中有效内容的长度（注意：筛选要求在原数组上进行）；
# (7) 编写函数 write_file 对 数组arr中的有效内容（即所有偶数）进行质因数分解，
# 并将 结果输出到屏幕和文本文件output.txt中。输出要求：每一个整数的质因数分解结果占一行，具体显示格式如下图所示：
# 4=2*2 ，952=2*2*2*7*17， 1334=2*23*29
import random

# 生成数据
def generateData(url):
    random.seed(100)
    res = [random.randint(0, 2768) for i in range(0, 100)]  # 测试数据
    
    with open(url, 'w+', encoding='utf8') as f:
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
        print('{0:6}'.format(alist[i]), end='')
        # 每行显示 n 个数, 每个整数占6列
        if (i+1) % n == 0:
            print('')
    print('')

# 统计数字0至9，在数组arr所有整数中的出现次数
def count(alist):
    res = [0 for i in range(0, 10)] # 0,1,....9
    length = len(alist)
    
    for i in range(0, length):
        num = list(str(alist[i]))   # 例：122-->['1', '2', '2']
        n_len = len(num)
        for j in range(0, n_len):
            res[int(num[j])] += 1
#    print(res)
    return res

# 因子和
def factor(num):
    res = 0
    for i in range(1, num + 1):
        if num % i == 0:
            res += i
    return res

# 因子和排序，一样，则按数字大小排序
def sort_array(alist):
    alist.sort(key=lambda x:(factor(x), x), reverse=True)
    return alist

# 保留所有的偶数，同时保证这些偶数按照从小到大排序。
# 前半部分是有效内容，即所有的偶数
# 后半部分则是无效内容，参数size记录了数组arr中有效内容的长度
def filter_array(alist):
    arr = list(filter(lambda x:x%2==0, alist))
    arr.sort()
    arr.append(len(arr))
    return arr

# 质因数分解
def filter_fac(n):
    i = 2
    res = []
    while i <= n:
        if n % i == 0:       # 从2开始筛选
            res.append(i)
            n /= i
        else:
            i = i + 1        
    return res

# 质因数分解输出
def write_file(arr):
    with open('./file/file_2019_out.txt', 'w', encoding='utf8') as f:
        for elem in arr:
            fac = filter_fac(elem)
            fac = list(map(str, fac))  # 每个质因数 -> str
            print('{0}={1}'.format(elem, '*'.join(fac)))
            f.write('{0}={1}\n'.format(elem, '*'.join(fac)))
    

def main():
    url = './file/file_2019_in.txt'
    generateData(url)
    # 第一问
    data = read_file(url)
    print_arr(data, 10)
    
    # 第二问
    res = count(data)           # 统计数字0至9  在数组arr所有整数中的出现次数
    print_arr(res, 5)
    
    # 第(5)问: 按因子和排序
    data = sort_array(data)
    print(data, "\n")

    # 第(6)问 保留偶数
    arr = filter_array(data)
    print(arr)
    
    # 第(7)问：质因数分解
    write_file(arr)
    
    
if __name__=='__main__':
    main()



























