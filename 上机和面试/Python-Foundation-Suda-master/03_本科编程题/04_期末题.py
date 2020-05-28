# 给定整数m和n，如果m和n都大于1，则判定m和n是否互质，并返回判定结果。

def func1():
    # 方法：2~t(t为m,n中较小的数) 分别除m和n，若能同时被除尽则互质。
    x, y = eval(input())
    if x <= 1 or y <= 1:
        return
    # 调整使得x < y
    if y < x:
        y, x = x, y
    
    temp = 2
    while temp<= x:
        if y%temp == 0 and x%temp==0:
            # print(temp)   # 输出最小公因数
            return True
        else:
            temp+=1
    else:
        return False


def func2():
    # 思路同上
    x, y = eval(input())
    if x <= 1 or y <= 1:
        return
    temp = 2
    while y%temp!=0 or x%temp!=0:
        if temp >x or temp>y:
            break
        temp += 1
    else:
        # print(temp)
        return True
    return False


"""
一个整数列表L=[a1, a2, …, an]中，
如果一对数(ai, aj)满足ai>aj且i<j，
那么这对数就称为一个逆序，
列表L中逆序的数量称为逆序数。
求一个整数列表L的逆序数。
"""

def func3():
    L = eval(input())
    res = 0
    for i in range(len(L)):
        for aj in L[i+1:]:
            res += 1 if L[i] > aj else 0
    print(res)
                
# if __name__ == "__main__":
#     func1()


"""
输入两个整数类型的矩阵mat1（m行d列）和mat2（d行n列），
返回矩阵相乘后的结果mat1*mat2（m行n列）。
矩阵均用二维列表进行表示。
[[1,2]]  1x2
[[1],[2]] 2x1

"""

def func4(mat1, mat2):
    """
    mat1 mxd, mat2 dxn
    return mxn
    """
    m = len(mat1)
    d = len(mat2[0])
    mat3 = []
    for row in range(m):
        mat3.append([]) # 为新矩阵添加一行
        for column in range(d):
            sum = 0     # 计算新矩阵新行的每一个元素值
            for r,c in zip(mat1[row],mat2[column]):
                sum += r*c
            mat3[row].append(sum)
    return mat3

# if __name__ == "__main__":
#     # mat1,mat2 = [[1,2]],[[1],[2]]
#     # mat1, mat2 = [[1,2],[1,3]], [[1,1],[1,0]]
#     mat1, mat2 = [[1,2],[1,3],[1,4]], [[1,1],[1,0]]
#     mat3 = func3(mat1,mat2)
#     print(mat3)


"""
一维列表转成二维列表： 
输入一个长度为n*n的一维列表， 返回一个n行n列的二维列表。
"""
import math

def func5(onedim:list):
    l = len(onedim)
    n = math.sqrt(l)
    if n%1 !=0:
        # 输入长度不是n*n
        return 
    else:
        n = int(n)
    ndim = []
    for i in range(n):
        ndim.append(onedim[i*n:i*n+n])
    return ndim

# if __name__ == "__main__":
#     while True:
#         l = eval(input())
#         n = func4(l)
#         print(n)


"""
给定一个字符串，包含了若干个以空格分开的单词，统计其中每个单词出现的次数，
以列表的形式返回其中出现次数最多的三个单词
（三者按照出现次数降序排序，当出现次数相同时，对单词按照字典序降序排序），
如果不足三个单词，则按照上述规则排序后全部返回。
"""

def countstr(string: str):
    str_list = string.split()
    str_dict = {}
    for word in str_list:
        str_dict[word] = str_dict.get(word,0) + 1
    str_list = sorted(str_dict, key=lambda x: str_dict[x], reverse=True)
    return str_list[:3]

# if __name__ == "__main__":
#     while True:
#         try:
#             string = input()
#             str_list = countstr(string)
#             print(str_list)
#         except:
#             break

"""
6.	仅包含 小写字母 的两个单词S和T的Jaccard系数（记为J）由如下三个统计量来确定：
令a是在两个单词中都出现的字母的个数，
b是在S中出现但没有在T中出现的字母的个数，
c是在T中出现但没有在S中出现的字母的个数，
那么J = a / (a + b + c)。给定两个单词S和T，

求确定其Jaccard系数的三个统计量a,b,c。
"""
def func6(S,T):
    import string
    a = b = c = 0
    for ch in string.ascii_lowercase:
        if ch in S and ch in T:
            a += 1
        elif ch in S:
            b += 1
        elif ch in T:
            c += 1
    return (a,b,c)


# if __name__ == "__main__":
#     S, T = eval(input())
#     print(func6(S, T))

"""
7.	统计一个非空字符串中出现次数最多的字符及其出现次数。
其中英语字母不区分大小写，全部统计为大写字母，
如’a’和’A’在计数时进行合并为’A’。
结果以包含字符和对应次数的列表形式进行返回。
"""
def func7(en_str:str)->list:
    frec = dict()
    for ch in en_str:
        frec[ch.upper()] = frec.get(ch.upper(),0) + 1
    highest = 0
    highkey = ''
    for k,v in frec.items():
        if v > highest:
            highkey,highest = k,v
    
    return (highkey,highest)
    
# if __name__ == "__main__":
#     s = input()
#     print(func7(s))

"""
8.	一个字符串中存在多个正整数，请提取出位数在[3,5]之间的所有正整数，
构成一个列表，对此列表按照数字和平均值（各位数字的总和/位数）进行降序排序，
并返回排序结果列表。数字和平均值就是各位数字的总和除以位数，
例如2345的数字和平均值=(2+3+4+5)/4=3.5，12的数字和平均值=(1+2)/2=1.5。
"""
def func8(num_str):
    import re
    pt = re.compile(r'\d+')
    num_list = filter(lambda x: 3<=len(x)<=5, pt.findall(num_str))
    num_list = list(map(int, num_list))
    def countnum(num):
        l = sum = 0
        while num:
            l += 1
            sum += num %10
            num //= 10
        return sum/l
    num_list.sort(key=countnum, reverse=True)
    return num_list


if __name__ == "__main__":
    print(func8(input()))