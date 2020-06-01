"""
如何在没有函数返回值的情况下， 原地删除列表中重复的元素
"""
from collections import Counter


def setmethod(L):
    temp_set = set(L)
    L.clear()
    L.extend(list(temp_set))


def setmethod2(L):
    # 不改变顺序
    t = sorted(set(L), key=L.index)
    L.clear()
    L.extend(t)


def popmethod(L):
    freq_dict = Counter(L)
    for index in range(len(L)-1, -1, -1):
        if freq_dict[L[index]] != 1:
            freq_dict[L[index]] -= 1
            L.pop(index)


def sortoddeven(L):
    # L.sort(reverse=True)
    # L.sort(key=lambda x: 1 if x % 2 == 0 else 0)
    L.sort(key=lambda x: (0 if x % 2 == 0 else 1, x), reverse=True)



if __name__ == "__main__":
    # L = [3, 2, 1, 4, 2, 5, 6, 3]
    # setmethod2(L)
    # print(L)
    # L = [3, 2, 1, 4, 2, 5, 6, 3]
    # popmethod(L)
    # print(L)

    L = [1, 2, 3, 4, 5, 6]
    sortoddeven(L)
    print(L)