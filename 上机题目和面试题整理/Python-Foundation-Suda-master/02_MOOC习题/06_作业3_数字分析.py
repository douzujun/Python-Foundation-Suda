"""
附件中有一个文本文件 Numbers.txt，文件中的每一行都是一个浮点数，编写程序读取出所有的浮点数。要求：

1 从小到大排序，将排序后的结果写到当前路径下新生成的一个文本文件
Sort.txt 中，每个数占一行。 

2 求出这些数字的均值、方差，将结果追加写到当前路径下新生成的一个文本
文件 Sort.txt 中，每个数占一行。 

3 要求生成的文本文件 Sort.txt 中同时包含排序和均值、方差的结果。
"""
floder = "./06_作业/"
input_path = floder + "Numbers.txt"
output_path = floder + "Sort.txt"


def get_nums(filename=input_path):
    # 获取浮点数
    f = open(filename, 'r')
    def trans(x): return float(x.strip())
    nums = list(map(trans, f.readlines()))
    f.close()
    return nums

def sort_output(nums, filename=output_path):
    # 排序并输出到文件
    f = open(filename, 'w')
    nums.sort()
    for num in nums:
        f.write(str(num)+'\n')
    f.close()

def avg_var_output(nums, filename=output_path):
    # 计算均值方差并输出
    avg = sum(nums)/len(nums)
    var = sum([(num - avg)**2 for num in nums])/len(nums)
    f = open(filename, 'a')
    f.write('avg:'+ str(avg) + '\n')
    f.write('var:'+ str(var) + '\n')
    f.close()

if __name__ == "__main__":
    nums = get_nums()
    sort_output(nums)
    avg_var_output(nums)
