import random
import time


def generate_random1(start, end, num):
    l = []
    while True:
        element = random.randint(start, end)
        if element not in l:
            l.append(element)
        if len(l) == num:
            break
    return l


def generate_random2(start, end, num):
    s = set()
    while True:
        s.add(random.randint(start,end))
        if len(s) == num:
            break
    return s


if __name__ == '__main__':
    start = time.time()
    for i in range(10000):
        l = generate_random2(1, 100, 50)
    print('time used:', time.time() - start)
