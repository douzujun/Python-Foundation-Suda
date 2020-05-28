f = open('test.bin', 'wb+')

f.write(b'12,34,53,25,61,28,78/n')

str1 = '中文/n测试/n'
bytes1 = bytes(str1, encoding='gbk')
f.write(bytes1)

f.seek(0)
bytes2 = f.read()
str2 = bytes2.decode('gbk', 'ignore')
print(str2)

f.close()

