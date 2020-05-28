import math


def bindivide(n: int):
    """
    二分法确定正整数n的平方根
    判断(start+end)/2的平方与n的大小关系
    """
    start, end = 0, n
    mid = 0
    while True:
        mid = (start+end)/2
        if abs(mid**2 - n) < 1e-6:
            break
        elif mid**2>n:
            end = mid
        else:
            start = mid
    return mid

def newton(n:int):
    # 牛顿迭代法
    pass


# abs((start+end)/2**2-n) > 1/(10*accruacy)

if __name__ == "__main__":
    n = int(input("输入一个正整数："))
    print("{}的平方根是{}".format(n, math.sqrt(n)))
    print(bindivide(n))
