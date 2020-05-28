# -*- coding: utf-8 -*-

def fun2():
    li = list(eval(input("输入列表: ")))
    
    Len = len(li)
    cnt = 0
    
    for i in range(0, Len):
        for j in range(i, Len):
            if (li[i] > li[j]):
                cnt = cnt + 1
    
    print(cnt)
    
fun2()