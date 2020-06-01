# 用穷举法找出1~100之间的勾股数
# 要求：不重复 e.g.345 就不要435 543
# 每行输出5组勾股数
# a^2+b^2=c^2
import math

def findgg1(start=1, end=100):
    l = []
    for i in range(start, end+1):
        for j in range(i, end+1):
            t = i + j if i + j <=100 else 100
            for k in range(i, t):
                if i**2 + j**2 == k**2:
                    l.append((i,j,k))
    print(l)

def findgg2(start=1, end=100):
    l = []
    for i in range(start, end+1):
        for j in range(i, end+1):
            k = math.sqrt(i**2 + j**2)
            if k%1 == 0 and k < 100:
                l.append((i,j,int(k)))
    print(l)


if __name__ == "__main__":
    findgg1()
    findgg2()
