"""
两个测试点通过，两个测试点格式错误
"""

def num2level(num):
    # 给定num返回 上半层最多一层的符号个数
    if num == 1:
        return 1, 0
    num, mod = divmod((num - 1), 2) # 上半部分的符号个数
    num += 1
    temp = 1
    while temp <= num:
        num -= temp
        temp += 2
    return temp-2, mod + num*2

def printgraph(long, ch):
    for i in range(long,-1,-2):
        print((ch*i).center(long,' '))
    for i in range(3, long+1, 2):
        print((ch*i).center(long, ' '))

if __name__ == "__main__":
    N, ch = input().split()
    N = int(N)
    temp,left = num2level(N)
    printgraph(temp, ch)
    print(left, end='')