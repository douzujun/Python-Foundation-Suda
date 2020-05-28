#-*- coding: utf8 -*-


def fun2(lst):
    # length = len(lst)
    # i, j = 0, length - 1
    # while i < j:
    #     while i < j and lst[j] % 2 == 0:
    #         j = j - 1
    #     while i < j and lst[i] % 2 == 1:
    #         i = i + 1
    #     if i < j:
    #         lst[i], lst[j] = lst[j], lst[i]

    # lst = sorted(lst[0:i+1]) + sorted(lst[i+1:])
    lst.sort(key=lambda x: (1 if x % 2 == 0 else 0, x))
    
    print(lst)

fun2([1,2,3,4,5,6,7])    
fun2([2, 3, 4, 5, 1, 3, 5, 7, 9])    
fun2([1, 2, 3, 6, 7, 10, 11])
