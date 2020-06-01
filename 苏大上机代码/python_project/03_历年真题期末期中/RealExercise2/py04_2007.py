# -*- coding: utf-8 -*-

# 把10 到 1000 之间满足以下两个条件的数，存搭配result.txt文件中
# 1. 是素数
# 2. 它的反数也是素数，如：123的反数是321
import math

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

# 123 的 反数是 321
def reverseNum(num):
    res = int(str(num)[::-1])
    return res

# 筛选素数
def filter_prime(start, end):
    return [i for i in range(start, end + 1)
            if is_prime(i) and is_prime(reverseNum(i))]


def saveFile(text):
    with open('./file/2007.txt', 'w', encoding='utf8') as f:
        f.write(str(text))
        
        
def main():
    res = filter_prime(10, 1000)
    print(res)
    saveFile(res)
    
    
if __name__=='__main__':
    main()



