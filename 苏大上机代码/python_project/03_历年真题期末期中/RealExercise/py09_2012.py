# -*- coding: utf-8 -*-

import struct

# 读取未知数字个数的二进制文件
def readFile(url):
    ans = []
    with open(url, 'rb+') as f:
        while True:
            data = f.read(4)
            if not data:
                break
            elem = struct.unpack('i', data)[0]
            ans.append(elem)
            
        return ans

# 将读取到的数构成坐标
def point(data):
    res = []
    len_data = len(data)
    for i in range(0, len_data, 2):
        comb = [data[i], data[i + 1]]
        res.append(comb)
    return res


# 有效点的个数
def validPoint(point):
    res = [elem for elem in point if (elem[0] > 0 and elem[1] > 0)]
    return res


# 横坐标的最小值 和 纵坐标的最小值 组成的矩阵
def minSquare(point):
    px, py = point[0][0], point[0][1] 
    len_p = len(point)
    for i in range(len_p):
        if px > point[i][0]:
            px = point[i][0]
        if py > point[i][1]:
            py = point[i][1]
    
    return px * py
        

# 横坐标最小的同时纵坐标也是最小(取最小值的下标是否一致)，返回满足条件的点
def minPoint(point):
    minx, miny = 0, 0
    len_p = len(point)
    for i in range(len_p):
        if point[minx][0] > point[i][0]:
            minx = i
        if point[miny][0] > point[i][1]:
            miny = i
    if minx == miny:
        return point[minx]
    else:
        return '不存在这样的点'


# 分组
def groupX(point : list):
    # 先按坐标x轴升序排列
    point.sort(key=lambda x : x[0])
    print(point)
    
    count = 0
    flag = [0 for i in range(len(point))]  # 标记数组初始化为0
    p_len = len(point)
    for i in range(p_len):
        if flag[i] == 0:                   # 首次被标记，归为下一个分组
            count += 1
            # 组数:count
            print('\ncount = ', count)
            print(point[i], end='')
            flag[i] = 1                    # 标志着已经使用过
            # t 为 第 t 组
            t = i
        for j in range(i + 1, p_len):
            if (flag[j] == 0) and (point[j][1] > point[t][1]) and (point[j][0] > point[t][0]):
                print(point[j], end='')
                flag[j] = 1
                t = j      
            


def main():
    data = readFile("./file/file_2012.txt")
#    print(data, "\n")
    
    p_point = point(data)
#    print(p_point)
    
    # 有效点的个数
    vapoint = validPoint(p_point)
    print(vapoint)
    print("有效点的个数 = {0}\n".format(len(vapoint)))
    
    print("最小公共区域面积 = {0}".format(minSquare(vapoint)))
    
    print("符合条件的点: ", minPoint(vapoint))
    
    groupX(vapoint)
    
    
    
if __name__ == '__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    