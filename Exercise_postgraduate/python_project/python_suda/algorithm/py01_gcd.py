# -*- coding: utf-8 -*-

num1, num2 = eval(input("请输入两个正整数"))

if num1 < num2:
    num1, num2 = num2, num1
    
while (num1 % num2):
    temp = num1 % num2
    num1 = num2
    num2 = temp

print("最大公约数：", num2)