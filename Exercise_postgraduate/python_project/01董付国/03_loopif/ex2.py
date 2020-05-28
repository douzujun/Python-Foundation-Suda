"""
生成一个包含50个随机整数的列表，删除其中的奇数
"""
import random
num_list = [random.randint(0,100) for _ in range(50)]
print(num_list)

for i in range(len(num_list))[::-1]:
    if num_list[i] % 2 != 0:
        del num_list[i]

print(num_list)