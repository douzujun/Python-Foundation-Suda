"""
附件中有一个文本文件 StrInts.txt，该文件中有一段英文文章，在该文章中存在一些整数（有正有负）。
编写程序读取该文件、并提取出其中所有的整数，然后将这些整数中 偶数位数字 上全部为 奇数数字 的整数保存到 
当前路径的ResultInts.txt 文件中去，保存时每行 3 个数、每个数占 8 列、右对齐左补空格
"""
import re

floder = "./06_作业/"
input_path = floder + 'StrInts.txt'
output_path = floder + 'ResultInts.txt'


def get_nums(filename):
    # 获取数字字符串组成的列表
    f = open(filename, 'r', encoding='utf-8')
    content = f.read()
    f.close()
    # 用正则匹配整数
    pattern = re.compile(r'\-?\d+')
    nums = pattern.findall(content)
    return nums

def issatisfy(num_str):
    # 判断是否满足偶数位数字全为奇数
    # 数字个位为 0 位   e.g. -2 不满足 -12满足
    for n in num_str[-1::-2]:
        if n not in ('1','3','5','7','9','-'):
            return False
    else:
        return True

def output_nums(output_path, nums):
    # 输出数字到文件
    f = open(output_path, 'w')
    i = 0
    for num in nums:
        print(num.rjust(8), end='', file=f)
        i += 1
        if i % 3 == 0:
            f.write('\n')
    f.close()


if __name__ == "__main__":
    nums = get_nums(input_path)
    nums = [num for num in nums if issatisfy(num)]  # 筛选满足条件的数字
    output_nums(output_path, nums)
    