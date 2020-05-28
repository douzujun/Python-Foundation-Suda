"""
附件中有一个文本文件 StrInts.txt，该文件中有一段英文文章，在该文章中存在一些整数（有正有负）。
编写程序读取该文件、并提取出其中所有的整数，然后将这些整数中 偶数位数字 上全部为 奇数数字 的整数保存到 
当前路径的ResultInts.txt 文件中去，保存时每行 3 个数、每个数占 8 列、右对齐左补空格
"""
import re

def readNums(url):
    with open(url, 'r', encoding='utf8') as f:
        content = f.read()
        
        nums = re.findall(r'\-?\d+', content)
        return nums

def judge(num):
    for n in num[-1::-2]:
        if not n in ['1', '3', '5', '7', '9', '-']:
            return False
    return True

def writeFile(url, nums):
    with open(url, 'w', encoding='utf8') as f:
        nlen = len(nums)
        for i in range(nlen):
            # f.write()不会自动加 \n
            f.write('{0:>8}'.format(nums[i]))
            if (i + 1) % 3 == 0:
                f.write('\n')
        f.write('\n')

def main():
    nums = readNums('./file/StrInts.txt')
    print(nums)
    nums = [num for num in nums if judge(num)]
    print(nums)
    writeFile('./file/ResultInts.txt', nums)

if __name__ == "__main__":
    main()