"""
用户输入小于1000的整数
对其进行因式分解
"""

x = int(input("输入小于1000的整数"))
temp = x
i = 2
result = []
while True:
    if temp == 1:
        break
    if temp%i == 0:
        result.append(i)
        temp = temp//i
    else:
        i += 1
print(x, '=', '*'.join(map(str, result)))
