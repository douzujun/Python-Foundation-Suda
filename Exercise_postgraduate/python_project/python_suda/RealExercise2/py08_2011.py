# -*- coding: utf-8 -*-

# 2011. 筛选素数
# 输出 1000-9999 中满足以下条件的所有数：
# 该数是素数.
# 十位数 和 个位数 组成的数是 素数， 百位数 和 个位数 组成的数是 素数.
# 个位数 和 百位数 组成的数是 素数，个位数 和 十位数 组成的数是 素数。 比如 1991 ，个位 和 十位 组成的数就是 19 .

import math

def is_prime(num):
    if num < 2:
        return False
    top = int(math.sqrt(num))
    i = 2
    while i <= top:
        if num % i == 0:
            return False
        i = i + 1
    return True

# 分割数字: 个位，十位，百位
def split(num):
    unit = num % 10             # 个位
    decade = (num // 10) % 10   # 十位
    hund = (num // 100) % 10    # 百位
    return [unit, decade, hund]

# 组成数
def comb(a, b):
    return a*10 + b

# 筛选素数
def filter_prime(start, end):
    res = [i for i in range(start, end + 1) if (is_prime(i)) and 
           (is_prime(comb(split(i)[1], split(i)[0]))) and
           (is_prime(comb(split(i)[2], split(i)[0]))) and
           (is_prime(comb(split(i)[0], split(i)[1]))) and
           (is_prime(comb(split(i)[0], split(i)[2])))]
    
    return res

def main():
    res = filter_prime(1000, 9999)
    print(res)
    
if __name__=='__main__':
    main()