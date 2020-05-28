"""
实现自己的my_bin() 10转2
“砝码”比较

编写my_hex(n)   10->16
hex2bin(n)  16->2
"""


def my_bin(n: int):
    L = []  #
    v = 1
    if n < 0:
        L.append('-')
        n = -n
    L.append('0b')
    while v <= n//2:
        # 找到大于 n//2的最小砝码
        v *= 2
    while v > 0:
        # 判断要不要添加该砝码
        if n < v:
            L.append('0')
        else:
            L.append('1')
            n -= v
        v //= 2
    return ''.join(L)


def my_hex(n: int):
    # 辗转相除法
    hex_char = ('0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f')
    L = []
    absn = abs(n)
    while absn > 0:
        L.append(hex_char[absn%16])
        absn //= 16
    L.append('0x')
    if n < 0:
        L.append('-')
    L.reverse()
    return ''.join(L)


def hex2bin(hex_str:str):
    """
    • 思路1：先将十六进制转换成十进制，再调用my_bin转成二进制
    • 思路2：直接将十六进制转换成二进制
    """
    # 思路一
    d = int(hex_str, 16)
    return my_bin(d)


if __name__ == "__main__":
    n = int(input())
    print(my_bin(n))
    print(my_hex(n))
    hex_str = input()
    print(hex2bin(hex_str))
