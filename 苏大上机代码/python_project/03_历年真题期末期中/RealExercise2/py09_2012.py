# -*- coding: utf-8 -*-

# 2012. 读取二进制文件 以及 左标
# org.dat 文件以 二进制方式 存放一系列整数，每个整数占 4 个字节.
# 从 第一个整数 开始，第一个整数 和 第二个整数 构成一个坐标点，以此类推，数据文件 中保存了 许多 坐标点数据.
# 规定处于 第一象限的坐标点 为 有效点，请问 数据文件 中 所有点的个数 n 为多少？ 有效点的个数 k 为多少？
# 每个 有效点 与 坐标原点 构成一个的 矩形，请问 k 个有效点 与 坐标原点 构成的 k 个矩形 的 最小公共区域面积为多少？
# 寻找 有效点 中 符合下列条件的点：
# 以该点为 坐标原点， 其它 有效点 ：
# 1. 仍然是 有效点， 即 处于第一象限 (不包括坐标轴上的点).
# 2. 输出这些点，对 所有有效点 进行分组，每个有效点 有且只有 属于一个分组，分组内的点 符合下列规则：
# 若 对组内所有点的 x，坐标进行排序。
# 点 p1(x1, y1) 在点 p2(x2, y2) 后面，即 x1 > x2 那么 y1 > y2 ，请输出所有的分组。

import struct

# 读取未知数字个数的二进制文件 struct
def readFile(url):
    ans = []
    with open(url, 'rb+') as f:
        while True:
            data = f.read(8)
            if not data:
                break
            elem = struct.unpack('2i', data)   # 读一个元组(x.y)
            ans.append(elem)
    return ans   

# 位于第一象限的坐标（有效点）
def validPoint(points):
    res = [elem for elem in points if (elem[0] > 0 and elem[1] > 0)]
    return res

# 最小公共区域面积 (横坐标的最小值 和 纵坐标最小值)组成的矩阵
def minSquare(points):
    px, py = points[0][0], points[0][1]
    len_p = len(points)
    for i in range(len_p):
        if px > points[i][0]:
            px = points[i][0]
        if py > points[i][1]:
            py = points[i][1]
    return px * py

# 分组有效点
# 对所有的 x 进行排序
# p1(x1, y1) 在点 p2(x2, y2) 后面，即 x1 > x2 那么 y1 > y2 
def groupX(points : list):
    # 先按坐标x 升序排序
    points.sort(key=lambda x : x[0])
    print(points)
    
    count = 0
    p_len = len(points)
    flag = [0 for i in range(p_len)]   # 标记数组初始化为0
    for i in range(p_len):
        if flag[i] == 0:               # 首次被标记，归为下一个分组
            count += 1
            # 组数：count
            print('\ncount = ', count)
            print(points[i], end = '')
            flag[i] = 1                # 标记着已经使用过
            # t 为 第 t 组
            t = i
        for j in range(i + 1, p_len):  # 比较 y
            # j 没有使用过
            if (flag[j] == 0) and (points[j][1] > points[t][1]) and \
               (points[j][0] > points[t][0]):
                   print(points[j], end='')
                   flag[j] = 1
                   t = j               # 逐个向后比较

def main():
    data = readFile('./file/file_2012.txt')
    print(data)
    
    # 有效点的个数
    vapoint = validPoint(data)
    print(vapoint)
    
    print("有效点的个数 = {0}\n".format(len(vapoint)))
    print("最小公共区域面积 = {0}\n".format(minSquare(vapoint)))
    groupX(vapoint)
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    