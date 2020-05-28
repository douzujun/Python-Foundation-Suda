# 1 字符串格式化
x = 1234
xo = "%o" % x   # 八进制
xh = "%x" % x   # 十六进制
xe = "%e" % x   # 指数e表示的浮点数

ord('你')       # Unicode字符序号
chr(20321)      # 序号->Unicode字符
"%s" % 65       # '65' 字符串
"%d, %c" % (65, 65) # 65, A 单个字符c
"%d" % '555'    # 字符串转换整数输出 （报错）要先int()
'%s' % [1,2,3]
str([1,2,3])

# format()
print("the number {0:,} in hex is: {0:#x}".format(5555,55))
print("the number {1:,} in oct is: {1:#o}".format(5555,55))
print("{name},{age}".format(name="Zachary", age="21"))
position = (5,8,11)
print("x{0[0]},y{0[1]},z{0[2]}".format(position))
weather=[('Monday','rain'),('Tuesday','sunny')]
formatter = "Weather of {0[0]} is {0[1]}".format
for item in map(formatter, weather):
    print(item)
for item in weather:
    print(formatter(item))

# 2 字符串常用方法
s = "apple,grape,orange"
s.find('g',2,8)
s.index('z')

s.split(',')        # ['apple', 'grape', 'orange']
s.rsplit(',')       # ['apple', 'grape', 'orange']
s.partition(',')    # ('apple', ',', 'grape,orange')
s.rpartition(',')   # ('apple,grape', ',', 'orange')

li = ['apple', 'peach', 'banana']
sep = ','
s = sep.join(li)

import timeit
timer1 = timeit.Timer('func1', 'from where import func1')
print(timer1.timeit(num))   # 次数

s = '中国，美国'
s.replace('中国', '中华人民共和国')

d = {'a':'b','b':'c'}
t = str.maketrans(d)        # 接受字典或两个等长字符串
'acc'.translate(t)

s = 'print("Hello World!")' 
eval(s)

# 生成随机8位长密码
import random, string
x = string.digits + string.ascii_letters + string.punctuation
p1 = ''.join([random.choice(x) for i in range(8)])
p2 = ''.join(random.sample(x,8))