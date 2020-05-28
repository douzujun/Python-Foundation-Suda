# -*- coding: utf-8 -*-

import re

# 生成字母
def generateAlpha():
    alpha_up = []
    alpha_low = []
    for i in range(26):
        alpha_up.append(chr(ord('A') + i))
    for i in range(26):
        alpha_low.append(chr(ord('a') + i))
        
    return [alpha_low, alpha_up]
    
# 加密
def encrapy(str1, n, alpha):
    alpha_low = alpha[0]      # 小写字母表
    alpha_up = alpha[1]       # 大写字母表
    length = len(str1)
    res = ""
    
    i = 0
    while i < length:
        num = ""
        if str1[i].isupper():
            res += alpha_up[(alpha_up.index(str1[i]) + n)%26]
            
        elif str1[i].islower():
            res += alpha_low[(alpha_low.index(str1[i]) + n)%26]
            
        elif str1[i].isnumeric():
            num += str1[i]
            i = i + 1
            while i < length and str1[i].isnumeric():
                num += str1[i]
                i = i + 1
            # 字符后退一个
            i = i - 1
            # 数字*n
            res += str(int(num)*n)
        
        i = i + 1
        
    return res

# 解密
def decode(str1, n, alpha):
    alpha_low = alpha[0]      # 小写字母表
    alpha_up = alpha[1]       # 大写字母表
    length = len(str1)
    res = ""
    
    i = 0
    while i < length:
        num = ""
        if str1[i].isupper():
            res += alpha_up[(alpha_up.index(str1[i]) - n)%26]
            
        elif str1[i].islower():
            res += alpha_low[(alpha_low.index(str1[i]) - n)%26]
            
        elif str1[i].isnumeric():
            num += str1[i]
            i = i + 1
            while i < length and str1[i].isnumeric():
                num += str1[i]
                i = i + 1
            # 字符后退一个
            i = i - 1
            res += str(int(num)//n)
        
        i = i + 1
        
    return res


def main():
    alpha = generateAlpha()
    
    str1 = 'avbV125av1'
    n = 5
    print("字符串:{0}, n默认为:{1}".format(str1, n))
    
    str2 = encrapy(str1, n, alpha)
    print("加密后:{0}".format(str2))
    
    str1 = decode(str2, n, alpha)
    print("解密后:{0}".format(str1))

if __name__=='__main__':
    main()

