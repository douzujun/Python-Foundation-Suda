"""
dn = pn+1 - pn  pi 为第i个素数
d1 = 1  对n>1有dn是偶数
素数对猜想认为存在无穷多相邻且差为2的素数

先给定任意正整数N（<10^5）请计算不超过N的满足猜想的素数对的个数

输入
N
输出个数
"""
# import sympy
import math

def is_prime_fast(num):
    if num <= 1:
        return False
    elif num == 2 or num == 3:
        return True
    elif num % 6 in (0, 2, 3, 4):
        return False
    else:
        half = int(math.sqrt(num)) + 1
        for i in range(5, half, 6):
            if num % i == 0 or num % (i+2) == 0:
                return False
        else:
            return True

def primes(max):
    pairs = 0
    prime_list = [i for i in range(1,max+1) if is_prime_fast(i)]
    if len(prime_list) in (0,1):
        print(0)
    else:
        i = 1
        l = prime_list[0]
        for i in range(1, len(prime_list)):
            c = prime_list[i]
            if c - l == 2:
                pairs += 1
            l = c
        print(pairs)

if __name__ == "__main__":
    while True:
        try:
            primes(int(input()))
        except:
            break


"""
n = int(input())
step = 2
contrast = [True] * (n + 2)
result = []

while step <= n:
    result.append(step)
    for i in range(step * 2, n + 1, step):
        contrast[i] = False
    while step <= n:
        step += 1
        if contrast[step]:
            break

print(len([i for i in range(len(result) - 1) if result[i + 1] - result[i] == 2]))
"""
