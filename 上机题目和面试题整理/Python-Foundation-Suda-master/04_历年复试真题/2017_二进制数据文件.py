r"""
2017
要求：
已知：二进制数据文件 data.bin 中存放了若干个整数，请编写程序完成如下功能：
1、编写程序读取所有数据.

2、以每相邻两个整数为一对按顺序构成二维平面上的坐标点. 例如：有数据 12 ， 34 ， 53 ， 25 ， 61 ，
28 ， 78 等，则构成六个坐标点如下： (12, 34) 、 (34, 53) ， (53, 25) ,  (25, 61) ,  (61, 28) ,  (28,
78) ；

3、以每个坐标点为圆心，以该点与其后面第一个点的欧氏距离为半径 r . 计算每个圆包含的坐标点数. 计算最后
一个点时以其和第一个点的欧氏距离为半径.
例如：
坐标点 (12, 34) 的圆半径$r=\sqrt{(12-34)^2+(34-53)^2}$是坐标点 (12, 34) 与 (34, 53) 的欧式距离.
坐标点 (28, 78) 的圆半径$r=\sqrt{(28-12)^2+(78-34)^2}$是坐标点 (28, 78) 与 (12, 34) 的欧式距离.
坐标点 包含点数 点密度
(x坐标，y坐标) (占5列，右对齐) (占7列，右对齐，保留2位小数)

4、计算所有圆的点密度值，然后输出点密度值最大的 5 个坐标点以及相应圆中包含的点数和点密度值. 输出格式

要求：
上述文字部分不需要显示.
其中：圆的点密度为圆包含的点数除以圆面积，如果点在圆上，则也算圆包含该点，在计算点密度时，圆心也算一
个点. 计算圆面积时$\pi=3.14$. 例如：坐标点 (2, 1) ，则该坐标点也属该坐标点的圆内的一个点.

"""
import math

pi = 3.14   

def get_num_list(filename:str):
    f = open(filename, 'rb')
    b = f.read()
    f.close()
    num_str = b.decode('gbk','ignore')
    return list(map(int, num_str.split(',')))

def get_cord(num_list:list):
    cord_list = []
    for i in range(0,len(num_list)-1):
        cord = tuple(num_list[i:i+2])
        cord_list.append(cord)
    return cord_list

def compute_dist(cord1, cord2):
    return math.sqrt((cord1[0]-cord2[0])**2 + (cord1[1]-cord2[1])**2)

def count_r_density(cord_list):
    length = len(cord_list)
    cord_dict = {}  # cord:[r,cord_num,density]
    for i in range(length):
        # 计算各个圆的半径
        cord_dict[cord_list[i]] = [compute_dist(cord_list[i],cord_list[(i+1)%length])]

    for k,v in cord_dict.items():
        # 计算每个圆包含的点数
        cord_num = 0
        for cord in cord_list:
            dist = compute_dist(k,cord)
            if dist <= v[0]:
                cord_num += 1
        cord_dict[k].append(cord_num)
        S = pi*(cord_dict[k][0]**2)
        cord_dict[k].append(S/cord_num)
    # print(cord_dict)
    return cord_dict

def print_result(cord_dict):
    # print(cord_dict)
    for k,v in cord_dict.items():
        s = '{0[0]},{0[1]} {1:>5} {2:>7.2f}'.format(k,v[1],v[2])
        print(s)

if __name__ == "__main__":
    filename = '2017_data.bin'
    num_list = get_num_list(filename)
    cord_list = get_cord(num_list)
    cord_dict = count_r_density(cord_list)
    print_result(cord_dict)