# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 14:32:20 2020

@author: douzi
"""


import struct

#读未知数字个数的二进制文件
def readFile(url):
    ls=[]
    with open(url, 'rb+') as f:
        while True:
            data = f.read(4)
            if not data:
                break
            elem = struct.unpack('i', data)[0]
            ls.append(elem)
        return ls

#将读取到的数构成坐标
def point(data):
    res=[]
    for i in range(0,len(data),2):
        ls=[data[i],data[i+1]]
        res.append(ls)
    return res

#有效点
def validPoint(point):
    res=[]
    for i in range(len(point)):
        if point[i][0]>0 and point[i][1]>0:
            res.append(point[i])
    return res

#横坐标的最小值和纵坐标的最小值组成的矩形
def minSquare(point):
    px,py=point[0][0],point[0][1]
    for i in range(len(point)):
        if px>point[i][0]:
            px=point[i][0]
        if py>point[i][1]:
            py=point[i][1]
    return px*py

#横坐标最小的同时纵坐标也是最小(取最小值时的下标是否一致)，返回满足条件的点
def minPoint(point):
    minx,miny=0,0
    for i in range(len(point)):
        if point[minx][0]>point[i][0]:
            minx=i
        if point[miny][1]>point[i][1]:
            miny=i
    if minx==miny:
        return point[minx]
    else:
        return '不存在这样的点'

#分组
def groupX(point):
    #先按坐标x轴升序排列
    point.sort(key=lambda x:x[0])
    count=0
    flag=[0 for i in range(len(point))] #标记数组初始化为0
    for i in range(len(point)):
        if flag[i]==0:                  #首次被标记，归为下一个分组
            count+=1
            print('\ncount=',count)
            print(point[i],end='')
            flag[i]=1
            t=i
        for j in range(i+1,len(point)):
            if flag[j]==0 and point[j][1]>point[t][1] and point[j][0]>point[t][0]:  #t用来记录上一次被标记的点下标
                print(point[j],end='')
                flag[j]=1
                t=j


if __name__=='__main__':
    data=readFile("./file/file_2012.txt")

    point=point(data)
    #print(point)

    vapoint=validPoint(point)
    print("有效点的个数=",len(vapoint))
    #print(vapoint)

    print("最小公共区域面积=",minSquare(vapoint))
    print('符合条件的点：',minPoint(vapoint))

    groupX(vapoint)








