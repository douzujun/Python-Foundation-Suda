"""
读取一个二进制数，里面有20k个数字。
求一个最大子集，将其写入到一个文件。
1. 最大子集任意两个数字之间不成倍数，且最大公约数为1
2. 按格式输入到一个文件中
格式：第一行为总个数
12
2 3 5 7 13
17 23 29 31 37
41 43
"""

def writetestnum(filename="2018_data.bin"):
    import random
    f = open(filename, 'wb')
    num_list = [random.randint(1,100) for _ in range(200)]
    i = 0
    while i < 200:
        temp = random.randint(1,15)
        if 200-i < temp:
            temp = 200-i
        f.write(bytes(str(temp)+'\n',encoding='gbk'))
        for _ in range(temp):
            f.write(bytes(str(num_list[i])+' ',encoding='gbk'))
            i += 1
        f.write(b'\n')



def readnum(filename="2018_data.bin"):
    f = open(filename, 'rb')
    bytestr = f.read()
    f.close()
    content = bytestr.decode('gbk','ignore')
    num_list = content.split()
    return num_list


def groupnum(num_list):
    pass


if __name__ == "__main__":
    # writetestnum()
    num_list = readnum()[:30]