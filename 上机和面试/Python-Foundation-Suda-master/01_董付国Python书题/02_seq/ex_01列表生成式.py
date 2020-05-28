"""
编写程序，生成包含1000个0~100之间的随机整数，并统计每个元素的出现次数。
"""

import random
num_list = [random.randint(0,100) for _ in range(1000)]
fre_dict = dict.fromkeys(range(0,101), 0)
for num in num_list:
    fre_dict[num] += 1
print(fre_dict)