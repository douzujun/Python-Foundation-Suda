import random as rd


def countbyset():
    # 使用集合
    l = [rd.randint(0, 100) for i in range(1000)]
    x = set(l)
    for i in x:
        print(i, l.count(i))


def countbydict():
    # 使用字典
    l = [rd.randint(0,100) for i in range(1000)]
    d = {}
    for i in l:
        d[i] = d.get(i, 0) + 1

    for k,v in d.items():
        print(k, v, sep=':')


if __name__ == '__main__':
    # countbyset()
    countbydict()