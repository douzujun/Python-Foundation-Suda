# -*- coding: utf-8 -*-

import struct

# 读取未知数字个数的二进制文件
def readFile(url):
    ans = []
    with open(url, 'rb+') as f:
        while True:
            data = f.read(8)
            if not data:
                break
            elem = struct.unpack('2i', data)
            ans.append(elem) 
    
    print(ans)
    return ans


def validPoint(points):
    validpoints = [elem for elem in points if (elem[0] > 0 and elem[1] > 0)]
    return validpoints

def minSquare(point):
    px, py = point[0][0], point[0][1]
    len_p = len(point)
    for i in range(len_p):
        if px > point[i][0]:
            px = point[i][0]
        if py > point[i][1]:
            py = point[i][1]
    return px * py
    
def groupPoints(points : list):
    points.sort(key=lambda x:x[0])
    print(points)
    
    cnt = 0
    plen = len(points)
    flag = [0] * plen
    for i in range(plen):
        if flag[i] == 0:
            cnt = cnt + 1
            print('\ncount = ', cnt)
            print(points[i], end='')
            flag[i] = 1                 # 标记已经使用过
            # t为第t组
            t = i
        for j in range(i + 1, plen):    # 找组内的坐标
            if (flag[j] == 0) and (points[j][1] > points[t][1]) and (points[j][0] > points[t][0]):
                print(points[j], end='') 
                flag[j] = 1 
                t = j                   # 组内 重新设置 t 坐标 

def main():
    points = readFile('./file/file_2012.txt')
    valpoints = validPoint(points)
    print(valpoints, len(valpoints))
    print("最小公共区域面积：", minSquare(valpoints))
    
    groupPoints(valpoints)
    
if __name__=='__main__':
    main()