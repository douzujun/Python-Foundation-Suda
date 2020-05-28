'''
2005
把一个数表示成若干个素数的和.
'''

import math
import string

def primeList(n):
    '''
    素数筛法
    primeL[i] = 1表示不是素数，相反为0表示是素数
    '''
    primeL = [0] * n
    m = int(math.sqrt(n + 1))
    
    for i in range(2, m + 1):
        if primeL[i] == 0:
            j = i * i
            while (j < n):
                primeL[j] = 1
                j += i
    return primeL
	
    
def main():
	num = eval(input())#输入所要表示的数值
	visit = primeList(10000)

	for i in range(1, num + 1):
		if visit[i] == 0:
			j = num - i
			if visit[j] == 0:
				print("{0} = {1} + {2}".format(num, i, j))
    
	
if __name__ == '__main__':
	main()
########################################

'''
2005
统计每篇文章中各英文字母的个数，并从大到小排序
'''

import math
import string


def main():
    with open('extent.txt', 'r', encoding = 'utf-8') as fp:
        alist = fp.readlines()
        s1 = ''.join(alist)
        
    d1 = dict()#存储 字母：次数
    slen = len(s1)
    for i in range(slen):
        if (s1[i] >= 'a' and s1[i] <= 'z'):
            d1[s1[i]] = d1.get(s1[i], 0) + 1
        if (s1[i] >= 'A' and s1[i] <= 'A'):
            d1[s1[i]] = d1.get(s1[i], 0) + 1
    
    list1 = list(d1.items())
    list1.sort(key = lambda x : x[1], reverse = False)#按次数排序
    
    for i, j in list1:
        print(i + '次数为：' + str(j))
        
if __name__ == '__main__':
    main()
    
##############################################

'''
2006
找出 100 到 1000 内的不含 9 的素数，存到 result 文件中.
'''

import math
import string


def primeList(n):
    '''
    素数筛法：
    返回一个列表，0表示是素数，1表示不是素数
    '''
    m = int(math.sqrt(n + 1))
    visit = [0] * n
    for i in range(2, m + 1):
        if visit[i] == 0:
            j = i * i
            while j < n:#不加=
                visit[j] = 1
                j += i
    return visit

def judge(num):
    '''
    判断num是否含有数字9，是就返回true，否则返回false
    '''
    alist = list(str(num))
    return '9' in alist

def main():
    primeL = primeList(1010)#数字可以适当地大一点
    alist = list()
    for i in range(100, 1000 + 1):
        if primeL[i] == 0 and (not judge(i)):
            alist.append(str(i))
    
    s = ' '.join(alist)
    with open('result.txt', 'w') as fp:
        fp.write(s)
    
if __name__ == '__main__':
    main()
    
##################################################

'''
2007
把 10 到 1000 之间满足以下两个条件的数，存到 result.txt 文件中.
1）是素数.
2）它的反数也是素数，如： 123 的反数是 321 .
'''

import math
import string

def primeList(n):
    '''
    素数筛法
    返回一个列表，0表示是素数，1表示不是素数
    '''
    visit = [0] * n
    m = int(math.sqrt(n + 1))#错了好几次，啦，一定要加int（）
    
    for i in range(2, m + 1):
        if visit[i] == 0:
            j = i * i
            while j < n:
                visit[j] = 1
                j += i
    return visit

def main():
    primeL = primeList(1010)
    
    alist = list()
    for i in range(10, 1000 + 1):
        t_list = list(str(i))
        t_list.reverse()
        reverse_i = int(''.join(t_list))
        
        if primeL[i] == 0 and primeL[reverse_i] == 0:
            alist.append(str(i))
    
    with open('result.txt', 'w') as fp:
        s = ' '.join(alist)
        fp.write(s)
        
if __name__ == '__main__':
    main()
    
##############################################

'''
2008
1.用 IE 从 FTP 上下载 org.dat ，并保存在 D 盘的根目录中.
2.此文件中按文本方式存放了一段其他文章，其中有若干长度小于 15 的英文单词，单词之间用空格分开，无其
他符号.
3.顺序读取这段文章的不同的单词(大小写敏感)，同时在读取的过程中排除所有的单词 THE 以及变形，即这些单
4.词不能出现在读取的结果中.
5.将读取的所有单词的首字母转大写后，输出 D 根目录下 new.txt ，每个单词一行.
org.dat内容如下：
The constructor is used to initialize the object The destructor is used to delete the Object the
calling seqence of constructor is opposite to the calling sequence of destructor.
'''
import string
import math
    
def main():
    with open('org.dat', 'r') as fp:
        context = fp.readlines()
        context = ''.join(context)
    
    alist = context.split()
    alist = list(map(lambda x : x.title(), alist))
    
    with open('new.txt', 'w') as fp:
        for item in alist:
            if item != 'The':
                fp.write(item + '\n')
    
if __name__ == '__main__':
    main()
	
###########################################################

'''
2009
1.用 IE 浏览器从 FTP 上下载 org2009.dat ，并保存在 D 盘的根目录下.
2.此文件中按文本方式存放了一段其他文章，其中有若干长度小于 15 的十进制或八进制数字，数字之间用 ,
分开，数字内部存在且仅存在空格.
3.八进制数以起始位 0 作为标示与十进制数区分.
4.顺序读取这些数字将他们转变为十进制数后按从大到小的顺序排序后，输出到 D 盘根目录下 new.txt ，每个
数字一行.
eg ： _235_,34__2,_043_1_,1_3 ，分别是：十进制 235 ，十进制 342 ，八进制 431 ，十进制 13 ， _ 代表
空格.
'''

import math
import string


def main():
    with open('org2009.dat', 'r') as fp:
        list1 = fp.readlines()
        s1 = ''.join(list1)
        
    list2 = s1.split(',')
    list2 = list(map(lambda x : x.strip(), list2))
    
    alist = []
    for item in list2:
        if item[0] == '0':
            alist.append(eval('0o' + item[1:]))
        else:
            alist.append(eval(item))
    alist.sort(reverse = False)

    with open('new2009.txt', 'w') as fp:
        for item in alist:
            fp.write(str(item) + '\n')
    
if __name__ == '__main__':
    main()
    
###############################################################

'''
2010
要求：
1.从 FTP 上下载 make.exe 和 org.dat ，运行 make.exe 输入准考证后三位生成 data.txt ，文件为二进制编码.
data.txt 内存有 2048 个整数，其中前 n 个为非 0 数，后 2048-n 个数为 0 ，将其读入数组，计算非零数的
个数 n .
2.选出 n 个数中的最大数和最小数.
3.选出 n 个数中最大素数.
4.将 n 个数从大到小排序，并平均分成三段(若 n 非 3 的整数倍，则不考虑最后的 1-2 个数)，选出中间段的最
大数和最小数.
输出格式：
n = 1000
min = 1
max = 4095
max_prime = 4093
min in mid_seg = 3630
max in mid_seg = 1863
'''

import math
import string

def judgePrime(x):
    '''
    function: 判断一个整数是否为素数
    input: 一个正整数 x
    output：如果x是素数，则返回ture， 否则返回false
    '''
    n = int(math.sqrt(x) + 1)
    for i in range(2, n + 1):
        if x % i == 0:
            return False
    return True

def main():
    #打开二进制文件读取数据
    dataL = list()
    with open('data.txt', 'rb') as fp:
        #假设数据存在多行
        temp1 = fp.readlines()
        temp2 = ''.join(temp1)
        f = lambda x : int(x)
        dataL = list(map(f, temp2.split()))
    
    #删除数据当中为0的数
    while dataL[-1] == 0:
        dataL.pop()
        
    n = len(dataL)
    minNum = min(dataL)
    maxNum = max(dataL)
    
    #得到数据当中的最大素数
    maxPrime = 0
    for item in dataL:
        if judgePrime(item):
            maxPrime = max(maxPrime, item)
    
    
    dataL.sort(reverse = True)
    
    #将数据的个数变成3的倍数
    temp = n % 3
    while temp > 0:
        dataL.pop()
    
    Len = len(dataL)
    m = Len // 3
    index = 2*m
    mid_dataL = dataL[m:index]
    
    mid_maxNum = max(mid_dataL)
    mid_minNum = min(mid_dataL)
    
    
    print('n = {0}'.format(n))
    print('max = {0}'.format(maxNum))
    print('min = {0}'.format(minNum))
    print('max_prime = {0}'.format(maxPrime))
    print('min in mid_seg = {0}'.format(mid_minNum))
    print('max in mid_seg = {0}'.format(mid_maxNum))
    
    
if __name__ == '__main__':
    main()
	
################################################


'''
2011
要求：
输出 1000-9999 中满足以下条件的所有数：
1、该数是素数.
2、十位数和个位数组成的数是素数，百位数和个位数组成的数是素数.
3、个位数和百位数组成的数是素数，个位数和十位数组成的数是素数. 比如 1991 ，个位和十位组成的数就是
19 .

'''

import math
import string

def JudgePrime(num):
    '''
    founction:判断一个正整数是否为素数
    input：输入一个正整数
    output：如果是素数返回True，否则返回False
    '''
    m = int(math.sqrt(num) + 1)
    for i in range(2, m + 1):
        if num % i == 0:
            return False
    return True

def main():
    for num in range(1000, 10000):
        #将四位数的数字分离
        d3, d2, d1, d0 = map(int, list(str(num)))
        
        d10 = d1 * 10 + d0
        d20 = d2 * 10 + d0
        d02 = d0 * 10 + d2
        d01 = d0 * 10 + d1
        
        if JudgePrime(num) and JudgePrime(d10) and JudgePrime(d20):
            if JudgePrime(d02) and JudgePrime(d01):
                print(num, end = ' ')
                
    print('\n')
        
    
if __name__ == '__main__':
    main()

########################################################


'''
2012
(最后一问不太确定)
要求：
1.从服务器上下载数据文件 org.dat 文件以二进制方式存放一系列整数，每个整数占 4 个字节. 从第一个整数
开始，第一个整数和第二个整数构成一个坐标点，以此类推，数据文件中保存了许多坐标点数据.
2.规定处于第一象限的坐标点为有效点，请问数据文件中所有点的个数 n 为多少？有效点的个数 k 为多少？
每个有效点与坐标原点构成一个的矩形，请问 k 个有效点与坐标原点构成的 k 个矩形的最小公共区域面积为
多少？
3.寻找有效点钟符合下列条件的点：以该点为坐标原点，其它有效点仍然是有效点即处于第一象限(不包括坐标
轴上的点). 输出这些点.
4.对所有有效点进行分组，每个有效点有且只有属于一个分组，分组内的点符合下列规则：若对组内所有点的x
坐标进行排序，点 p1(x1, y1) 在点 p2(x2, y2) 后面，即 x1>x2 那么 y1>y2 ，请输出所有的分组.

'''

import math
import string


def main():
    #读取文件，保存数据
    dataL = list()
    with open('org2012.dat', 'rb') as fp:
        s1 = fp.readline()
        list1 = list(map(lambda x : eval(x), s1.split()))
        xlist = list1[::2]
        ylist = list1[1::2]
        dataL = list(zip(xlist, ylist))#存储点数据
        
    n = len(dataL)#全部点的个数
    
    #删除不在第一象限的点
    for item in dataL[::]:
        if item[0] <= 0 or item[1] <= 0:
            dataL.remove(item)
    k = len(dataL)#有效点的个数
    
    xlist = list(map(lambda x : x[0], dataL))
    ylist = list(map(lambda x : x[1], dataL))
    xlist.sort()
    ylist.sort()
    MinPublicS = xlist[0] * ylist[0] #最小公共面积
    
    dataL.sort()
    x, y = dataL[0] #符合所有点都在改点的右上方的点 
    
    print('n = {0}\nk = {1}\nmin area = {2}'.format(n, k, MinPublicS))
    print('符合条件的点：', (x, y))
    
    while len(dataL) > 0:
        print('point group by:', end = ' ')
        
        temp = dataL[0]
        print(temp, end = ' ')
        dataL.remove(temp)
        
        for item in dataL[::]:
            if item[0] > temp[0] and item[1] > temp[1]:
                print(item, end = ' ')
                temp = item
                dataL.remove(item)
        print()
    
    
if __name__ == '__main__':
    main()


####################################################


'''
2014
要求：
1.从网页上下载 input.dat 文件，里面是用二进制编写的，里面放了一堆 int 型的数，每个数占 4 个字节，每
次读取两个，这两个数构成一个坐标.
2.规定处于第一象限的数是有效点(即 x>0, y>0 的坐标)，问这么多点中有效点有多少个？
3.现在用户从键盘输入一个坐标和一个数字 k ，设计算法输出 k 个离该坐标距离最近的点的坐标和每个坐标到
该点的距离，写入到 output.txt 文件中.

'''

import math
import string

def Diction(x1, y1, x2, y2):
    '''
    founction:计算两点之间的距离
    input：分别输入两点的坐标值（int）
    output：输出两点之间的距离（float）
    '''
    x = abs(x1 - x2)
    y = abs(y1 - y2)
    return math.sqrt(x * x + y * y)
    

def main():
    dataL = []
    with open('input2014.dat', 'rb') as fp:
        s1 = fp.readline()
        list1 = list(map(lambda x : eval(x), s1.split()))
        xlist = list1[::2]
        ylist = list1[1::2]
        dataL = list(zip(xlist, ylist))#j将数据变成坐标的形式存储
    
    #去除坐标点当中不在第一象限的无效点
    for item in dataL[::]:
        if item[0] <= 0 or item[1] <= 0:
            dataL.remove(item)
    n = len(dataL) #有效点的个数
    print('有效点的个数k = ' + str(n))
    
    #用户输入三个整数分别表示：x, y, k
    inputs = input('请输入一个坐标和一个数字k：')
    x, y, k = map(eval, inputs.split())
    
    dictionL = []
    for item in dataL:
        dictionL.append(Diction(x, y, item[0], item[1]))
    
    xlist = list(map(lambda x : x[0], dataL))
    ylist = list(map(lambda x : x[1], dataL))
    xydList = list(zip(xlist, ylist, dictionL))
    
    xydList.sort(key = lambda x : x[2])#根据两点之间距离从小到大排序
    
    #将距离最近的k个点和对应的距离写入文件当中
    with open('output2014.txt', 'w') as fp:
        for i in range(k):
            item = xydList[i]
            fp.write('x = {0}, y = {1}, d = {2}\n'.format(item[0], item[1], item[2]))
    
    
    
if __name__ == '__main__':
    main()
	
##################################################################

'''
2016
要求：
文本文件 input.txt 由若干英文单词和分隔符(空格，回车，换行)构成. 根据如下说明编写程序统计不同单词出现
的次数(频度). 将统计结果按出现频度从高到低排序，并将出现频度大于 5 的单词及其频度输出到文件 output.txt
中. 文件格式如下所示：
WinEdt, 31
'''

import math
import string


def main():
    words = []
    #读取文件，将单词存储到words列表当中
    with open('input2016.txt', 'r') as fp:
        slist = fp.readlines()
        s1 = ' '.join(slist)
        words = s1.split()
    
    #统计每个单词的词频
    setWord = list(set(words))
    count = []
    for item in setWord:
        count.append(words.count(item))
    
    word_count_list = list(zip(setWord, count))
    word_count_list.sort(key = lambda x : x[1], reverse = True)
    
    #把频度不大于五的去掉
    while word_count_list[-1][1] <= 5:
        word_count_list.pop()
    
    #将数据存储文件当中
    with open('output2016.txt', 'w') as fp:
        for item in word_count_list:
            fp.write('{0}, {1}\n'.format(item[0], item[1]))
    
    
if __name__ == '__main__':
    main()
	
###################################################################



'''
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
'''
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
    with open('data2017.bin', 'rb') as fp:
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