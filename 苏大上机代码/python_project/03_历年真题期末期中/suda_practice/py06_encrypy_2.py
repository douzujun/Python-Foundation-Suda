# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import re

    
# 加密
def encrapy(str1, n):
    words = re.findall('\d+|[a-zA-Z]+|\W+', str1)
    res = ''
    
    for word in words:
        if word.isnumeric():
            res += str(int(word)*n)
        elif word.isalpha():
            for c in word:
                k = ord(c) + n
                if ord('Z') < k < ord('a') or k > ord('z'):
                    res += chr(k - 26)
                else:
                    res += chr(k)
        
    return res

# 解密
def decode(str1, n):
    words = re.findall('\d+|[a-zA-Z]+|\W+', str1)
    res = ''
    
    for word in words:
        if word.isdigit():
            res += str(int(word)//n)
        elif word.isalpha():
            for c in word:
                k = ord(c) - n
                if k < ord('A') or ord('Z') < k < ord('a'):
                    res += chr(k + 26)
                else:
                    res += chr(k)
    return res


def main():
    
    str1 = 'avbV125av1'
    n = 5
    print("字符串:{0}, n默认为:{1}".format(str1, n))
    
    str2 = encrapy(str1, n)
    print("加密后:{0}".format(str2))
    
    str1 = decode(str2, n)
    print("解密后:{0}".format(str1))

if __name__=='__main__':
    main()

