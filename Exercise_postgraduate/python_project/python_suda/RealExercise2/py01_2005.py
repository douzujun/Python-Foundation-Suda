# -*- coding: utf-8 -*-

# 2005. 把一个数表示成若干个素数的和
# 如：9-->[7, 2]
import math

# 判断素数
def is_prime(num):
    # 小于2则不是素数
    if num < 2:
        return False
    
    top = int(math.sqrt(num))   # 设置上限
    i = 2
    while i <= top:
        if num % i == 0:
            return False
        i = i + 1
    return True


# 素数结果
res = []
# 从大到小 筛选素数
# 递归 筛选
def split_prime(num):
    if num < 2:
        return 
    
    if is_prime(num):
        res.append(num)
        return
    
    # 从大到小筛选素数
    for i in range(num, 1, -1):
        if (is_prime(i) and num - i > 1):
            res.append(i)
            split_prime(num - i)
            return    

# 测试用例
def faction_prime():
    while True:
        num = int(input())
        split_prime(num)
        print(res)
        # 清除上次结果
        res.clear()
    
def main():
    faction_prime()
    
    
if __name__=='__main__':
    main()


















    