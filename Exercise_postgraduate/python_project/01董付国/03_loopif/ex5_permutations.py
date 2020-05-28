"""
输出所有由 1 2 3 4四个数字组成的素数
并且在每个素数中每个数字只使用一次
"""
import itertools as it
import sympy

for seq in it.permutations(range(1,5),4):
    num = int(''.join(map(str,seq)))
    if sympy.isprime(num):
        print(num)