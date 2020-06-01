# 写出一个程序，接受一个由字母和数字组成的字符串，和一个字符，
# 然后输出输入字符串中含有该字符的个数。不区分大小写。

from sys import stdin as std
str1 = std.readline().strip().lower()
char2 = std.readline().strip().lower()
print(str1.count(char2))
