# -*- coding: utf-8 -*-



# 埃氏筛选法
def judge():
    n = int(input())
    res = 0
    
    is_prime = [True]*(n+1)
    is_prime[0] = is_prime[1] = True
    
    
    # 筛选出所有素数 
    primes = []
    for i in range(2, n+1):
        if is_prime[i]:
            primes.append(i)
            j = 2*i
            while j <= n:             # 将 i 的倍数全部划去
                is_prime[j] = False
                j += i
           
    
    for i in range(2, n - 1):
        if is_prime[i] and is_prime[i+2]:
            res += 1
    
    print(res)
    
    
judge()
    
    
    
    