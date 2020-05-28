# -*- coding: utf-8 -*-
"""
Created on Thu Apr  9 22:43:01 2020

@author: douzi
"""

import struct
import math

def readFile(url):
    wds = """2 88 59 83 87 65 38 72 70 76 50 62 4 76 68 70 50 60 13 74 66 60 8 28 97 94 99 52 6 90 69 60 54
83 76 89 64 73 48 69 83 28 84 67 14 50 99 86 35 36 5 82 67 36 92 99 44 27 53 76 24 45 27 19 14
65 86 69 47 80 96 96 10 68 60 91 87 25 15 50 8 18 3 15 85 88 14 8 2 64 63 62 70 58 62 93 51 66
62 73 75 6"""
    with open(url, 'rb+') as f:
        line = wds.split()
        for i in line:
            elem = struct.pack('i', int(i))
            f.write(elem)
        
    res = []
    with open(url, 'rb+') as f:
        while True:
            data = f.read(8)
            if not data:
                break
            elem = struct.unpack('2i', data)
            res.append(elem)
        
    return res

def distance(a, target):
    return math.sqrt((abs(a[0] - target[0])**2) + (abs(a[1] - target[1])**2))


def density(count, r):
    return count / (r*r*math.pi)

def main():
    points = readFile('./file/file_2017.txt')
    print(points)

    plen = len(points)
    circle = []          # 距离
    
    for i in range(plen):
        circle.append(distance(points[i], points[(i+1)%plen]))
    
    # 计算每个圆中包含的点数
    count = [0 for i in range(0, plen)]    # 圆包含的点数
    for i in range(0, plen):
        for j in range(0, plen):
            if (distance(points[i], points[j]) - circle[i] <= 1e-7):
                count[i] += 1
        
    # 求点密度
    densitys = []
    for i in range(plen):
        densitys.append(density(count[i], circle[i]))
        
    combine = []
    for i in range(0, plen):
        combine.append([points[i], count[i], densitys[i]])
    
    combine.sort(key=lambda x:x[2], reverse=True)
    for i in range(5):
        print("坐标点:{0}, 包含点数:{1:>5}, 点密度:{2:>7.2f}".format(combine[i][0], combine[i][1], combine[i][2])) 
    
    
if __name__=='__main__':
    main()
    






















