"""
生成一个包含20个随机整数的列表，
然后对其偶数下标的元素进行降序排序，
奇数下标的元素位置不变。
"""

import random
num_list = [random.randint(0,100) for _ in range(20)]
print(num_list)
print("偶数下标", num_list[::2])
num_list[::2] = sorted(num_list[::2], reverse=True)
print(num_list)
print("偶数下标", num_list[::2])
