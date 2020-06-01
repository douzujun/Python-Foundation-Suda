# -*- coding: utf-8 -*-

# 从 FTP 上下载 make.exe 和 org.dat ，运行 make.exe 输入准考证后三位
# 1. 生成 data.txt 文件为二进制编码 data.txt ，内存有 2048 个整数.
# 2. 其中 前n个为 非0数，后 2048 - n 个数为 0 ，将其读入数组，计算 非零数 的 个数 n. 
# 3. 选出 n 个数中的最大数和最小数，选出 n 个数中最大素数.
# 4. 将 n 个数从大到小排序，并平均分成三段(若 n 非 3 的整数倍，则不考虑最后的 1-2 个数)，
# 5. 选出中间段的最大数和最小数.

# n = 1000
# min = 1
# max = 4095
# max_prime = 4093
# min in mid_seg = 3630
# max in mid_seg = 1863
import math
import random
import struct

def is_prime(num):
    if num < 2:
        return False
    top = int(math.sqrt(num))
    i = 2
    while i <= top:
        if num % i == 0:
            return False
        i = i + 1
        
    return True              


def main():
    res = [random.randrange(0, 9999, 1) for i in range(0, 32)]
#    print(res)
    
#    with open('./file/2010.txt', 'rb+') as f:
#        for i in res:
#            s = struct.pack('i', i)
#            f.write(s)
    
    # 写多少数据，一定要弄清楚
    len1 = len(res)
    nums = []
    with open('./file/2010.txt', 'rb+') as f:
        for i in range(len1):
            data = f.read(4)
            elem = struct.unpack('i', data)[0]
            nums.append(elem)
    
    
    # 按照 16进制 转换成 10进制        
    nums.sort(reverse=True)
    print("Max:", nums[0], " Min:", nums[-1])
    
    print("数据数:", len1, nums)
    for i in nums:
        if (is_prime(i)):
            print("最大素数: ", i)
            break
    
    mid = nums[len1//3 : len1//3*2]
    print("mid_start:", mid[0], " mid_end:",  mid[-1])  
        


if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    