# -*- coding: utf-8 -*-

# 文本文件 input.txt 里面放了一堆整数，仅仅以空格分隔，
# 其中第一个整数为 k ，第二个整数代表维度，剩余的整数作为点的坐标.
#- 读取整数 k 和维度，并读取剩余的整数组成指定维度的点.
#- 从所有点中找到距离最近的两个点并输出它们的坐标和距离.
#- 分别输出距离这两个点最近的 k 个点的坐标 .
import struct
import random
import math


def GenerateData(url):
    random.seed(100)
#    res = (random.randint(2,20000) for i in range(0, 20000))
#    res = [11, 3, 5, 7, 9, 12, 33, 31, 4, 11]
    res = [2,3,5,7,13,17,23,29,31,37,41,43, 9]
#    res = [i for i in range(1, 500)]
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
           
def writeFile(data, length):
    with open("./file/file_2018_output.txt", 'w+', encoding='utf8') as f:
        for i in range(0, length, 5):
            if data[i:i+5]:
                f.write(str(data[i:i+5]) + "\n")
            

def gcd(num1, num2):
    if num1 < num2:
        num1, num2 = num2, num1
    
    while (num1 % num2):
        temp = num1 % num2
        num1 = num2
        num2 = temp
        
    return num2

def filter_list(data, length):
    
    res = []
    print(data)
    
    flag = [1 for i in range(0, length)]
    for i in range(0, length):
        for j in range(i+1, length):
#            print(data[i], data[j])
            if gcd(data[i], data[j]) != 1:
                flag[j] = 0          # flag设置为0，标志为不可用
                flag[i] = 0          
                break
        if flag[i] and (j == length - 1) and (gcd(data[i], data[j-1]) == 1):
            res.append(data[i])
            print("res:", res)    
            
    res = list(set(res))             # 去重
    print(res, len(res))
    return res


def main():
    url = './file/file_2018_input.txt'
   
    GenerateData(url)    
    data = readFile(url)
    
    length = len(data)
    res = filter_list(data, length)
    
    writeFile(res, length)

    
main()




















