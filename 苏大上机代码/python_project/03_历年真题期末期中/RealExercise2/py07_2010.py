# -*- coding: utf-8 -*-

# 生成 data.txt 文件为二进制编码 data.txt ，内存有 2048 个整数.
# 其中 前 n 个为非 0 数，后 2048 - n 个数为 0 ，将其读入数组，计算 非零数 的 个数 n.
# 选出 n 个数中 的 最大数 和 最小数，选出 n 个数中 最大素数.
# 将 n 个数 从大到小排序，并 平均分成三段 (若 n 非 3 的整数倍，则不考虑最后的 1-2 个数)，
# 选出 中间段的 最大数和最小数.
import math
import random
import struct

# 判断素数
def is_prime(num):
    if num < 2:
        return False
    top = math.sqrt(num)
    i = 2
    while i <= top:
        if num % i == 0:
            return False
        i = i + 1
    return True

# 生成数据--读写文件
def generateFile(url):
    # 测试用例
    res = [random.randrange(0, 9999) for i in range(0, 16)]
#    print(res)
    # 写入文件(二进制): struct
    with open(url, 'rb+') as f:
        for i in res:
            s = struct.pack('i', i)
            f.write(s)
    
    len1 = len(res)
    nums = []
    with open('./file/2010.txt', 'rb+') as f:
        for i in range(len1):
            data = f.read(4)
            elem = struct.unpack('i', data)[0]   # 获取的是元组
            nums.append(elem)
    return nums

def main():
    nums = generateFile('./file/2010.txt')
    print(nums)
    
    # 排序, 降序
    nums.sort(reverse=True)
    # 非零数的个数 n
    nums = [e for e in nums if e > 0]
    print("非零数的个数: ", len(nums))
    print("n个数的最大：{0}, 最小：{1}".format(nums[0], nums[-1]))
    for i in nums:
        if (is_prime(i)):
            print("最大素数: ", i)
            break
    # 平均分成三段
    len1 = len(nums)
    mid = nums[len1//3 : len1//3*2]
    # 中间段的最大数 和 最小数
    print(mid[0], mid[-1])
        
    
if __name__=='__main__':
    main()
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    