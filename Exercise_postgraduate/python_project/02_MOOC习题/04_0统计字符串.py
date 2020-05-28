

f = open("test.txt", 'rt')
data = f.readlines()
f.close()

dic = dict()
for line in data:
    line = line.upper()
    for c in line:
        if "A" <= c <= "Z":
            dic[c] = dic.get(c, 0)+1

i = 0
for k in sorted(dic):
    # 按键排序
    print("%s:%d\t"%(k, dic[k]), end='')
    i += 1
    if i% 4 ==0:
        print("")

i = 0
for k in sorted(dic, key=dic.__getitem__, reverse=True):
# for k in sorted(dic, key=lambda x:dic[x], reverse=True):
    # 按值排序
    print("%s:%d\t"%(k, dic[k]), end='')
    i += 1
    if i% 4 ==0:
        print("")
