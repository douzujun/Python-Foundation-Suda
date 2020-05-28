"""
给定一个k位整数N = dk-1 * 10^k-1 + ... + d1 * 10^1
(0<=di<=9, i=0,...,k-1,dk-1>0)
编写程序统计每种不同的各位数字出现的次数
例如给N=100311则有2个03个1和1个3

每个输入包含1个测试用例，即一个不超过1000位的正整数N
对N中每一种不同的个位数字，以D:M的格式在一行中输出D及其次数M
要求按D的升序输出
"""

def count_num(N):
    num_dict = {}
    for ch in N:
        num_dict[ch] = num_dict.get(ch, 0) + 1
    
    return num_dict

if __name__ == "__main__":
    N = input()
    num_dict = count_num(N)
    num_list = sorted(num_dict)
    for num in num_list:
        print("{}:{}".format(num, num_dict[num]))
