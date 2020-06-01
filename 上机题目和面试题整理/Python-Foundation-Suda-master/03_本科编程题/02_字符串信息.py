import re
import random

def get_sting(filename='./Files/02_string.txt'):
    # 未要求从文件中读取，为了方便将字符串存于文件中
    f = open(filename, 'r')
    target = f.read()
    f.close()
    return target.strip()


def get_primes(string):
    # 获得包含3 7的数字
    pattern = r'\d+'
    num_list = [num for num in re.findall(
        pattern, string) if '3' in num or '7' in num]
    num_list = list(map(int, num_list))

    def isprime(num):
        # 判断是否是素数
        if num >= 2:
            for i in range(2, int(num**(1/2)+1)):
                if num % i == 0:
                    return False
            else:
                return True
        else:
            return False

    for index in range(len(num_list)-1, -1, -1):
        if not isprime(num_list[index]):
            num_list.pop(index)

    # 输出部分
    nextline = False
    for num in num_list:
        print('{}'.format(num).rjust(10), end='')
        if nextline:
            print('')
            nextline = False
        else:
            nextline = True
    if len(num_list) % 2 == 1:
        # 奇数个数字最后额外换行
        print('')

    return num_list


def get_cord(nums):
    cords = []
    for index in range(0, len(nums), 2):
        if index+1 < len(nums):
            cords.append(nums[index: index+2])
    print("素数构成了{}个坐标：".format(len(cords)), cords)
    return cords


def randomA():
    x = random.randint(0, 100)
    y = random.randint(0, 100)
    print('生成的随机(x,y)为: ({: >10.2f}, {: >10.2f})'.format(x, y))
    return (x, y)


def compute_dist(cords, xy):
    dis_sum = 0
    for cord in cords:
        dis_sum += ((cord[0]-xy[0])**2 + (cord[1]+xy[1])**2)**(1/2)
    print('坐标点到A的欧氏距离和：{: >10.2f}'.format(dis_sum))
    print('坐标点到A的平均距离为: {: >10.2f}'.format(dis_sum/(len(cords))))


def countASCII(target):
    pattern = r'[a-zA-Z]{2,}'   # 长度大于2的连续字母
    words = re.findall(pattern, target)
    length_list = []
    for word in words:
        temp = 0
        for ch in word:
            temp += ord(ch)
        length_list.append(temp)
    
    # 输出部分
    print('单词转换整数:')
    count = 0
    for length in length_list:
        count += 1
        print('{: <8}'.format(length), end='')
        if count == 10:
            print('')
            count = 0


if __name__ == "__main__":
    target = get_sting()
    nums = get_primes(target)
    cords = get_cord(nums)
    xy = randomA()
    compute_dist(cords, xy)
    countASCII(target)
