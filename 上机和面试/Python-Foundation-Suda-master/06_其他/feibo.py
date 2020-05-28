"""
测试
"""

class fb:
    num_list = []
    def __init__(self):
        self.num_list.extend(1, 1)

    def __str__(self):
        return self.num_list


def f1(n):
    # 递归法
    a, b = 1,1
    if n > 2:
        for _ in range(2, n):
            a, b = b, a+b
    return b


def f2():
    # 生成器
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == "__main__":
    a = f2()
    for i in range(10):
        print(a.__next__(), end=',')

    print(f1(10))
