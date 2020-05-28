# -*- coding: utf-8 -*-


# 给定两个字符串 s 和 t，它们只包含小写字母。字符串 t 由字符串 s 随机重排，
# 然后在随机位置添加一个字母。请找出在 t 中被添加的字母。
def func4(str1, str2):
    s = sorted(str1)
    t = sorted(str2)
    slen = len(s)
    tlen = len(t)
    
    for i in range(0, slen):
        if s[i] != t[i]:
            return t[i]
        
    return t[tlen - 1]        
    
def main():
    print(func4('abcd', 'abcde'))
    
    print(func4('abcd', 'aebcd'))
    
    print(func4('abcd', 'abecd'))
    
    print(func4('abbcd', 'abbecb'))
    
    
main()
    