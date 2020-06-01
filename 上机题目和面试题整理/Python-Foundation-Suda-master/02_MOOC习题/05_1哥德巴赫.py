"""
哥德巴赫猜想：任一大于2的偶数都可以写成2个质数之和

fast_goldbach  (sympy.isprime)

goldbach 与上作比较
"""
import math
import sympy
from time import perf_counter

def is_prime(n: int):
    # 判断是否是质数
    if n >= 2:
        for i in range(2, int(math.sqrt(n) + 1)):
            if n % i == 0:
                return False
        return True
    else:
        # 质数要大于1
        return False


def goldbach(n: int, speed='D'):
    prime = is_prime if speed == 'D' else sympy.isprime
    if n <= 2 or n%2 !=0:
        print("n must greater than 2 and n%2 == 0")
    for p in range(2, n):
        q = n - p
        if prime(p) and prime(q):
            print("{}={}+{}".format(n,p,q))
            break
    else:
        print("There is something wrong.")


if __name__ == "__main__":
    while True:
        try:
            print("="*10)
            n = int(input("input n: "))
            mode = input("fast or default F or D: ")
            start = perf_counter()
            goldbach(n, mode)
            print(mode, 'cost:', perf_counter()-start)
        except Exception as e:
            print(e)
