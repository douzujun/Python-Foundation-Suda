# -*- coding: utf-8 -*-
"""
Created on Sun Mar 29 19:47:25 2020

@author: douzi
"""

import re

def solve():
    n = int(input())
    i = 0
    
    for i in range(n):
#        密码必须由不少于6个字符组成，并且只能有英文字母、数字和小数点 . ，还必须既有字母也有数字
        pwd = input()
        
        plen = len(pwd)
        sign = re.findall('[^0-9a-zA-Z.]', pwd)      # 存在不合法字符
        num = re.findall('[0-9]', pwd)              # 是否只有字母
        alpha = re.findall('[a-zA-Z]', pwd)         # 是否只有数字
        
        if plen < 6:
            print("Your password is tai duan le.")
        elif sign:
            print("Your password is tai luan le.")
        elif num == []:
            print("Your password needs shu zi.")
        elif alpha == []:
            print("Your password needs zi mu.")
        else:
            print("Your password is wan mei.")
            
        
solve()
        