# -*- coding: utf-8 -*-

# 从网页上下载 input.dat 文件，里面是用二进制编写的，里面放了一堆 int 型的数，
# 每个数占 4 个字节，每次读取两个，这两个数构成一个坐标.
# 规定处于第一象限的数是有效点(即 x>0, y>0 的坐标)，问这么多点中有效点有多少个？
# 现在用户从键盘输入一个坐标和一个数字 k ，设计算法输出 k 个离该坐标距离最近的点的坐标和每个坐标到
# 该点的距离，写入到 output.txt 文件中

import struct
import math

def readFile(url):
    res = []
    with open(url, 'rb+') as f:
        while True:
            data = f.read(8)
            if not data:
                break
            elem = struct.unpack('2i', data)
            res.append(elem)
            
    return res
        

def validPoint(data):
    res = [elem for elem in data if (elem[0] > 0 and elem[1] > 0)]
    return res

def distance(a, target):
    return math.pow(abs(a[0]-target[0]), 2) + math.pow(abs(a[1]-target[1]), 2)
    
def writeFile(sorted_vap, target, k):
    with open("./file/file_2014_output.txt", 'w', encoding='utf8') as f:
        for i in range(0, k):
             f.write("{0} -> 目标{1} 距离: {2:.2f}\n".format(sorted_vap[i], target, math.sqrt(distance(sorted_vap[i], target))))

def main():
    data = readFile('./file/file_2014.txt')
    print(data)
    
    vapoint = validPoint(data)
    print("\n有效点: ", vapoint)
    print("有效点数目: ", len(vapoint))
    
    k = int(input("输入k:"))
    x = int(input("输入坐标x:"))
    y = int(input("输入坐标y:"))
    target = (x, y)
    print(target)
    
    sorted_vap = sorted(vapoint, key=lambda x:distance(x, target))
    print(sorted_vap)
    
    
    print("k个坐标距离target的距离：")
    for i in range(0, k):
        print("{0} -> 目标{1} 距离: {2:.2f}".format(sorted_vap[i], target, math.sqrt(distance(sorted_vap[i], target)) ))
    
    writeFile(sorted_vap, target, k)
        

if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    