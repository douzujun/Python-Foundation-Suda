# -*- coding: utf-8 -*-

# 2018.真题(不确定)
# 有20000个数存储于二进制文件中，读取出来-
# 然后求一个最大子集，其中两两互相不为倍数，不为约数，最大公约数为1
# 然后满足的数据输出到指定文件中。
import struct
import random
import math

# 生成数据
def generateData(url):
    random.seed(100)     # 设置随机数种子
    # 测试数据
    res = [2, 3, 5, 7, 13, 17, 23, 29, 31, 37, 41, 43, 11, 9, 25]
#    res = (random.randint(2,20000) for i in range(0, 20000))
    
    # 写数据
    with open(url, 'wb+') as f:
        for elem in res:
            s = struct.pack('i', elem)
            f.write(s)

# 读数据
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
    
# 写文件
def writeFile(data, length):
    with open('./file/file_2018_output.txt', 'w+', encoding='utf8') as f:
        for i in range(0, length, 5):
            if data[i:i+5]:
                f.write(str(data[i:i+5]) + '\n')
                
# 如果要手写gcd，求 最大公约数
def gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    
    while (num1 % num2):
        temp = num1 % num2
        num1 = num2
        num2 = temp
    
    return num2
    
# 求一个最大子集
# 其中两两互相不为倍数，不为约数，最大公约数为1
def filter_list(data, length):
    res = []
    print(data)
    
    # 标志
    flag = [1 for i in range(0, length)]
    for i in range(0, length):
        for j in range(i + 1, length):
            # 如果两个数最大公约数不为1，则这两个数剔除
#            print(data[i], data[j])
            if (math.gcd(data[i], data[j]) != 1):
                flag[j] = 0       # flag设置为0，标志为不可用
                flag[i] = 0
                break
        # 如果 最后一个元素才break 且 倒数第一和元素i 最大公约数为1，则添加data[i]
        if flag[i] and (j == length - 1) and (math.gcd(data[i], data[j]) == 1):
            res.append(data[i])
    
    # 如果所有元素都遍历完，且最后一个元素，没有被标志
    if flag[i] and (i == length - 1):
        res.append(data[i])
        
    return res
    
def main():
    url = './file/file_2018.txt'
    generateData(url)
    # 读文件
    data = readFile(url)
    
    length = len(data)
    res = filter_list(data, length)
    print(res)
    
    writeFile(res, length)
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    

