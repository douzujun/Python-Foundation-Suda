# -*- coding: utf-8 -*-

import math
import string

def Diction(x1, y1, x2, y2):
    '''
    founction:计算两点之间的距离
    input：输入两个坐标点，坐标点的值都是整数
    output：输出一个距离，为float型
    '''
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    return math.sqrt(x * x + y * y)

def main():
    
    #读取数据
    dataL = []
    with open('./file/file_2017.txt', 'rb+') as fp:
        s1 = fp.readline()
        dataL = list(map(lambda x : eval(x), s1.split()))
    
    #将数据编程点数据
    temp1 = len(dataL) - 1
    xlist = dataL[:temp1]
    ylist = dataL[1:]
    pointT = list(zip(xlist, ylist)) #存储点数据
    pointT.append((dataL[-1], dataL[0]))
    pointT = tuple(pointT)
    
    dictM = [] #存储两点之间的距离，是一个矩阵
    for point1 in pointT[::]:
        temp = []
        for point2 in pointT[::]:
            temp.append(Diction(point1[0], point1[1], point2[0], point1[1]))
        dictM.append(temp)
    dictM = tuple(dictM)
    
    result = []
    for i in range(len(pointT)):
        temp = []
        temp.append(pointT[i])
        num = 0 #包含的点数（带圆心）
        
        index1 = (i + 1) % len(pointT)
        r = dictM[i][index1] #半径
        
        for d in dictM[i]:
            if d <= r:
                num += 1
        temp.append(num - 1)
        
        pidu = num / (3.14 * r * r) #点密度
        temp.append(pidu)
        result.append(temp)
        
    for item in result:
        point = item[0]
        print('({0}, {1})'.format(point[0], point[1]), end = ' ')
        print('%5d' % item[1], end = ' ')
        print('%7.2f' % item[2])

    
if __name__ == '__main__':
    main()