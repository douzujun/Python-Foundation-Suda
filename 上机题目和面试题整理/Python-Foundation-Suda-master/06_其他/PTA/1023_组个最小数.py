"""
给定数字 0-9 各若干个。你可以以任意顺序排列这些数字，但必须全部使用。
目标是使得最后得到的数尽可能小（注意 0 不能做首位）。
例如：给定两个 0，两个 1，三个 5，一个 8，我们得到的最小的数就是 10015558。
现给定数字，请编写程序输出能够组成的最小的数。

输入在一行中给出 10 个非负整数，顺序表示我们拥有数字 0、数字 1、……数字 9 的个数。
整数间用一个空格分隔。
10 个数字的总个数不超过 50，且至少拥有 1 个非 0 的数字。
"""

def f():
    num_list = list(map(int, input().split()))
    first = 0
    for i in range(1, len(num_list)):
        if num_list[i] != 0:
            first = i
            num_list[i] -= 1
            break
        i += 1
    else:
        print('0')
        return
    print(first,end='')
    current = 0
    for num in num_list:
        for i in range(num):
            print(current, end='')
        current += 1

if __name__ == "__main__":
    f()