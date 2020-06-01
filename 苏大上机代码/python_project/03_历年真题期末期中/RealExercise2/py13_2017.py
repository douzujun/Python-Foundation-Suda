# -*- coding: utf-8 -*-

# 2017.py
# 以每相邻两个整数为一对按顺序构成二维平面上的坐标点. 例如：有数据 12 ， 34 ， 53 ， 25 ， 61 ， 28 ， 78 等，则构成六个坐标点如下： (12, 34) 、 (34, 53) ， (53, 25) , (25, 61) , (61, 28) , (28, 78) ；
# 以 每个坐标点为圆心，以 该点 与 其后面第一个点 的 欧氏距离为半径 r . 计算 最后一个点 时 以其 和第一个点 的欧氏距离为半径。
# 计算 每个圆包含的坐标点数.
import struct
import math

def readFile(url):
    # 测试用例
    wds = """2 88 59 83 87 65 38 72 70 76 50 62 4 76 68 70 50 60 13 74 66 60 8 28 97 94 99 52 6 90 69 60 54
83 76 89 64 73 48 69 83 28 84 67 14 50 99 86 35 36 5 82 67 36 92 99 44 27 53 76 24 45 27 19 14
65 86 69 47 80 96 96 10 68 60 91 87 25 15 50 8 18 3 15 85 88 14 8 2 64 63 62 70 58 62 93 51 66
62 73 75 6"""
    # 写文件
    with open(url, 'wb+') as f:
        line = wds.split()
        for i in line:
            elem = struct.pack('i', int(i))
            f.write(elem)
    
    res = []
    # 读文件
    with open(url, 'rb+') as f:
        while True:
            data = f.read(8)
            if not data:
                break
            elem = struct.unpack('2i', data)  # 读一个元组(x,y)
            res.append(elem)
    return res

# 计算欧式距离
def distance(a, target):
    return math.sqrt(math.pow(abs(a[0] - target[0]), 2) + math.pow(abs(a[1] - target[1]), 2))

# 计算 圆的点密度
def density(count, r):
    return count / (r*r*math.pi)

def main():
    points = readFile('./file/file_2017.txt')
    
    polen = len(points)
    
    circle_radius = []   # 存储距离(当作圆半径)
    # 以每个坐标点为圆心，以 该点 与 其后面第一个点 的欧氏距离为半径 r
    # 计算每个圆包含的坐标点数. 计算 最后一个点 以其和 第一个点 的欧氏距离为半径.
    for i in range(0, polen):
        circle_radius.append( distance(points[i], points[(i+1)%polen]) )
    
    
    # 计算 每个圆包含的 坐标点数
    count = [0 for i in range(0, polen)]   # 圆包含的点数
    for i in range(0, polen):
        for j in range(0, polen):
            # 坐标i 和 其他坐标j 距离 
            if (distance(points[i], points[j]) - circle_radius[i] <= 1e-8):
                count[i] += 1              # 圆心为i,radius[i]的圆, 包含的坐标 数
    
    # 计算所有圆的点密度值，然后输出 点密度值 最大的 5 个坐标点
    # 圆的点密度：圆包含的点数 / 圆面积
    densitys = []
    for i in range(0, polen):
        densitys.append( density(count[i], circle_radius[i]) )
        
    # 输出 点密度值 最大的 5 个坐标点
    # 输出格式:
    # 坐标点(x,y)  包含点数(占5列,右对齐)  点密度(占7列，右对齐，保留2位小数)
    combine = []
    for i in range(0, polen):
        combine.append([points[i], count[i], densitys[i]])
    
    # 根据点密度排序
    combine.sort(key=lambda x:(x[2]), reverse=True)
    for i in range(0, 5):
        print("坐标点:{0}, 包含点数:{1:>5}, 点密度:{2:>7.2f}".format(combine[i][0], combine[i][1], combine[i][2]))
    
    
if __name__=='__main__':
    main()









