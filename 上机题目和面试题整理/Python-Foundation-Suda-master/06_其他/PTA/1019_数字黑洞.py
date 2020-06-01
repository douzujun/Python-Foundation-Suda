"""
给定任一个各位数字不完全相同的 4 位正整数，
如果我们先把 4 个数字按 非递增排序 ，(减)
再按非递减排序(增)，然后用第 1 个数字减第 2 个数字，将得到一个新的数字。

一直重复这样做，我们很快会停在有“数字黑洞”之称的 6174，这个神奇的数字也叫 Kaprekar 常数。

现给定任意 4 位正整数，请编写程序演示到达黑洞的过程。
"""

def show_process(int_list):
    # ['7', '7','6','6']
    while int_list != list('6174'):
        int_list1 = sorted(int_list,reverse=True)
        int_list2 = sorted(int_list)
        int1 = int(''.join(int_list1))
        int2 = int(''.join(int_list2))
        int3 = int1 - int2
        int_list = list(str(int3))
        print('{:4d} - {:04d} = {:04d}'.format(int1, int2, int3))


if __name__ == "__main__":
    int_list = list(input())
    if len(set(int_list)) == 1:
        print('{0:04d} - {0:04d} = 0000'.format(int(''.join(int_list))))
    else:
        show_process(int_list)
    