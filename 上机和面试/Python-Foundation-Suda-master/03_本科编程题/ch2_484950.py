
def no48():
    weight = (65.5, 70.2, 100.5, 45.5, 88.8, 55.5, 73.5, 67.8)

    avg = sum(weight) / len(weight)
    cov = sum([pow(w-avg, 2) for w in weight]) / len(weight)

    print(cov)

def no49(dic1, dic2):
    for k in dic1:
        if k in dic2.keys():
            print(k, end=' ')

def no50(dic1,dic2):
    for v in dic1.values():
        if v in dic2.values():
            print(v, end=' ')

if __name__ == "__main__":
    # 49
    # d1 = {1:2, 2:3}
    # d2 = {1:3, 3:1}
    # no49(d1,d2)

    # 50
    # d1 = {1:2, 2:3}
    # d2 = {1:3, 3:1}
    # no50(d1,d2)

    pass