# -*- coding: utf-8 -*-

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

def validPoint(points):
    res = [elem for elem in points if (elem[0] > 0 and elem[1] > 0)]
    return res

def distance(a, target):
    return math.pow(abs(a[0] - target[0]), 2) + math.pow(abs(a[1] - target[1]), 2) 
    

def writeFile(sorted_vap, target, k):
    with open("./file/file_2015_output.txt", 'w', encoding='utf8') as f:
        for i in range(0, k):
             f.write("{0} -> 目标{1} 距离: {2:.2f}\n".format(sorted_vap[i], target, math.sqrt(distance(sorted_vap[i], target))))


def main():
    points = readFile("./file/file_2015.txt")
    vapoints = validPoint(points)
    print(vapoints)
    valen = len(vapoints)
    print("有效点的个数: ", valen)
    
    k = int(input("输入k:"))
    n = int(input("输入n:"))
    x = int(input("输入坐标x:"))
    y = int(input("输入坐标y:"))
    target = (x, y)
    
    sorted_vap = sorted(vapoints, key=lambda x:(distance(x, target)))
    print("k个坐标距离target的距离：")
    for i in range(0, valen):
        dis = math.sqrt(distance(sorted_vap[i], target))
        if dis < n:
            print("{0} -> 目标{1} 距离: {2:.2f} 小于{3}".format(sorted_vap[i], target,  dis, n))
    
    writeFile(sorted_vap, target, valen)
    
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    