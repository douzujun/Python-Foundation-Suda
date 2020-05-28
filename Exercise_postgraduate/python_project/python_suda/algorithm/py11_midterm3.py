# -*- coding: utf-8 -*-

def fun2(lst):
    length = len(lst)
    i = 0
    j = length - 1
    while i < j:
        while i < j and lst[j] % 2 == 0:   # 后面是偶数
            j = j - 1
        if i < j:
            t = lst[j] 
        while i < j and lst[i] % 2 == 1:   # 前面是奇数
            i = i + 1
        if i < j:
            lst[j] = lst[i]
            lst[i] = t
        
    print(lst)


def main():
    fun2([1,2,3,4,5,6])
    fun2([1, 2, 3, 6, 7, 10, 11])
    fun2([2, 3, 4, 5, 1, 3, 5, 7, 9])
    fun2([2,4,6,8,10, 1,3,5,7,9])

main()