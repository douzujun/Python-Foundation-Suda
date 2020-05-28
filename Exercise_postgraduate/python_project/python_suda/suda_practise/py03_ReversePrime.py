# -*- coding: utf-8 -*-

# (反素数)反素数指一个素数将其逆向拼写后也是一个素数的非回文数。
# 例如：17 和 71 都是素数且都不是回文数，所以 17 和 71 都是反素数。
# 请编写一个函数判断一个数是否是反素数？并编写测试程序找出前 30 个反
# 素数输出到屏幕上，要求每行输出 8 个数，每个数占 5 列，右对齐。

import math
# 素数
def is_prime(num):
    if num < 2:
        return False
    top = math.sqrt(num)
    i = 2
    while i <= top:
        if num % i == 0:
            return False
        i = i + 1
    return True


def Reverse(num):
    return int(str(num)[::-1])

def print_res(res, length):
    for i in range(0, length):
        print("{0:>5}".format(res[i]), end='')
        if (i+1)%8 == 0:
            print('')
    print('')

def main():
    cnt = 0
    cur = 2
    res = []
    while cnt < 30:
        if is_prime(cur) and is_prime(Reverse(cur)):
            res.append(cur)
            cnt = cnt + 1
        cur = cur + 1
        
    print_res(res, len(res))
    
if __name__=='__main__':
    main()    

