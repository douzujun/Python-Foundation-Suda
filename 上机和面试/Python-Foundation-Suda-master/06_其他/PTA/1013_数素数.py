"""
Pi：第i个素数  给M<=N<=10^4 输出Pm到Pn的所有素数

输入一行给MN 空格分离
输出所有素数 10个数字一行 空格分离 行末无多余空格
"""

from math import sqrt

def is_prime_fast(num):
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 6 in (0, 2, 3, 4):
        return False
    else:
        half = int(sqrt(num)) + 1
        for i in range(5, half, 6):
            if num % i == 0 or num % (i+2) == 0:
                return False
        else:
            return True

def generat_prime(M, N):
    prime_list = []
    prime_no, current = 0, 1
    while prime_no <= N:
        current += 1
        if is_prime_fast(current):
            prime_no += 1
            if M <= prime_no <= N:
                prime_list.append(current)

    return prime_list


def print_list(prime_list):
    i = 1
    for num in prime_list[:-1]:
        if i % 10 == 0:
            print(num)
        else:
            print(num, end=' ')
        i += 1
    else:
        # 输出最后一个
        if len(prime_list) >= 1:
            print(prime_list[-1])


if __name__ == "__main__":
    while True:
        try:
            M, N = map(int, input().split())
            prime_list = generat_prime(M, N)
            print_list(prime_list)
        except Exception as e:
            break


# def is_prime(num:int):
#     if num <= 1:
#         return False
#     else:
#         for i in range(2, int(sqrt(num))+1):
#             if num % i == 0:
#                 return False
#         else:
#             return True
