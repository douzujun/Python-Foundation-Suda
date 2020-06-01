
d = {'a': 1, 'b': 2}
while True:
    k = input('请输入键')
    if k == '':
        break
    else:
        print(d.get(k, '您输入的键不存在'))
