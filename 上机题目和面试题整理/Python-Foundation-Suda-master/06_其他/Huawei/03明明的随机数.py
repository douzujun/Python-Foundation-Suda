# N个1~1000的随机数
# 对于重复数字指保留一个，去掉其他相同的数
# 对这些数从小到大排序
import sys

s = set()
lines = sys.stdin.readlines()
linenum = 0
result = []
while linenum < len(lines):
    n = int(lines[linenum].strip())
    for line in lines[linenum + 1:linenum + n + 1]:
        s.add(int(line.strip()))
    result.extend(sorted(s))
    s.clear()
    linenum += n + 1

for item in result:
    print(item)


# 注意多组数据的输入！

def method2():
    while True:
        try:
            n = int(input())
            l = [int(input()) for _ in range(n)]
            l = sorted(set(l))
            for i in l:
                print(i)
        except:
            break