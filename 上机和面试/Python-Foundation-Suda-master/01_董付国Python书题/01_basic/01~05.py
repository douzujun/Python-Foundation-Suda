import math

def func1():
    a, b = eval(input("input a,b:"))
    res = divmod(a, b)
    print('{0[0]}, {0[1]}'.format(res))

def func2():
    name = input("input your name:")
    print(len(name))

def func3():
    pi = 3.14
    h, r = eval(input())
    v = h * pi * r ** 2
    d, m = divmod(20, v)
    if m :
        print('{}'.format(int(d+1)))
    else:
        print(d)

def func4():
    x1,y1 = eval(input("x1,y1"))
    x2,y2 = eval(input("x2,y2"))
    dis = ((x1-x2)**2 + (y1-y2)**2)**0.5
    print(dis)

def func5():
    import random
    num = random.randint(100,999)
    print(num)
    s = str(num)
    s2 = ''.join(reversed(s))
    print(s2)

if __name__ == "__main__":
    # func1()
    # func2()
    # func3()
    # func4()
    func5()
    pass