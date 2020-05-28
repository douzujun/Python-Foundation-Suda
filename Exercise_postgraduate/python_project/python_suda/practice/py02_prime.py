# -*- coding: utf-8 -*-

import math

def prime():
    num = int(input("请输入一个数:"))

    top = int(math.sqrt(num))
    
    i = 2
    
    while i <= top:
        if num % i == 0:
            break
        i = i + 1
        
    if (i == top + 1) and num > 1:
        print(num, "是素数.")
    else:
        print(num, "不是素数.")
        

while True:
    prime()
    


    
