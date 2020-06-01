# -*- coding: utf-8 -*-

#编写一个函数，将一个整数的各位数字对调，并编写测试程序，
#在测试函数中输入整数和输出新的整数。
#例如：输入 123，调用该函数之后，得到结果为 321
def reverse_num(num):
    res = int(str(num)[::-1])
    return res

def main():
    print(reverse_num(12345))
    
if __name__=='__main__':
    main()
    
    