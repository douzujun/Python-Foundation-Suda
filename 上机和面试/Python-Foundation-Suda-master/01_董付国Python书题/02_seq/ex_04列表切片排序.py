"""
生成20个随机数的列表，然后将前10个元素升序排列，后10个降序排列
"""

import random

num_list = [random.randint(0,100) for _ in range(20)]
print(num_list)
num_list[0:10] = sorted(num_list[0:10])
num_list[10:20] = sorted(num_list[10:20], reverse=True)
print(num_list)