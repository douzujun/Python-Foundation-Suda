# 方法一
import sys

line = sys.stdin.readline().strip().split()[-1]
print(len(line))

# 方法二
s = input()
print(len(s.split()[-1]))